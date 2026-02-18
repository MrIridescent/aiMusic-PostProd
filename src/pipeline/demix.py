import torch
import torchaudio
import logging
import os
from demucs import pretrained
from demucs.apply import apply_model
from demucs.separate import load_track

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class AudioDemixer:
    """
    Handles high-fidelity source separation using Demucs.
    """
    def __init__(self, model_name="htdemucs_ft", device=None):
        self.device = device or ("cuda" if torch.cuda.is_available() else "cpu")
        try:
            logger.info(f"Initializing Demucs model '{model_name}' on device: {self.device}")
            self.model = pretrained.get_model(model_name)
            self.model.to(self.device)
            self.model.eval()
        except Exception as e:
            logger.error(f"Failed to initialize Demucs model: {e}")
            raise

    def separate(self, audio_path):
        """
        Separates a flattened stereo track into isolated stems.
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
        
        try:
            logger.info(f"Loading track: {audio_path}")
            wav = load_track(audio_path, self.model.audio_channels, self.model.samplerate)
            wav = wav.to(self.device)
            
            logger.info("Applying source separation model...")
            with torch.no_grad():
                sources = apply_model(self.model, wav[None], shifts=1, split=True, overlap=0.25, progress=True)[0]
                
            sources = sources.cpu()
            stems = {name: sources[i] for i, name in enumerate(self.model.sources)}
            return stems, self.model.samplerate
        except Exception as e:
            logger.error(f"Error during separation of {audio_path}: {e}")
            raise

    def save_stems(self, stems, samplerate, output_dir):
        """
        Saves separated stems to disk.
        """
        try:
            os.makedirs(output_dir, exist_ok=True)
            for name, stem in stems.items():
                path = os.path.join(output_dir, f"{name}.wav")
                torchaudio.save(path, stem, samplerate)
                logger.info(f"Saved {name} to {path}")
        except Exception as e:
            logger.error(f"Failed to save stems: {e}")
            raise

if __name__ == "__main__":
    # Example usage (can be used for testing)
    import sys
    if len(sys.argv) > 1:
        demixer = AudioDemixer()
        stems, sr = demixer.separate(sys.argv[1])
        demixer.save_stems(stems, sr, "output_stems")
