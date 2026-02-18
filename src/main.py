import os
import torch
import torchaudio
import numpy as np
from src.pipeline.demix import AudioDemixer
from src.pipeline.restoration import AudioRestorer, VocalNaturalizer
from src.pipeline.mixing import MixingEngine
from src.agents.conductor import AIConductor

class AIPostProductionPipeline:
    """
    Orchestrates the complete AI music post-production pipeline.
    """
    def __init__(self, output_dir="output"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)
        self.demixer = AudioDemixer()
        self.restorer = AudioRestorer()
        self.vocal_nat = VocalNaturalizer()
        self.mixing_engine = MixingEngine()
        # Conductor is optional/experimental in this implementation
        self.conductor = AIConductor()

    def process(self, audio_path):
        """
        Runs the full pipeline: Demix -> Restore -> AI Mix -> Master.
        """
        print(f"--- Stage I: Source Separation for {audio_path} ---")
        stems, sr = self.demixer.separate(audio_path)
        
        print("--- Stage II: Neural Audio Restoration ---")
        restored_stems = {}
        for name, stem in stems.items():
            # Apply denoising and restoration
            print(f"Restoring {name}...")
            if name == "vocals":
                # Deep denoising and humanization for vocals
                vocal_enhanced = self.restorer.denoise_vocal(stem, sr)
                vocal_arr = vocal_enhanced.numpy()
                vocal_nat = self.vocal_nat.humanize(vocal_arr, sr)
                vocal_nat = self.vocal_nat.mask_quantization(vocal_nat, sr)
                restored_stems[name] = vocal_nat
            else:
                # Standard restoration and prep for super-resolution
                restored_stems[name] = self.restorer.prepare_for_audiosr(stem, sr).numpy()

        print("--- Stage III & IV: AI-Driven Mixing ---")
        # In a real nuanced scenario, we'd loop with the Conductor here
        # For now, we apply the mixing engine directly
        final_mix = self.mixing_engine.mix_stems(restored_stems)
        
        # Export final result
        output_path = os.path.join(self.output_dir, "final_master.wav")
        # Ensure final_mix is a tensor for torchaudio saving
        if isinstance(final_mix, np.ndarray):
            final_mix = torch.from_numpy(final_mix)
        
        # Reshape if necessary (channels, samples)
        if final_mix.ndim == 1:
            final_mix = final_mix.unsqueeze(0)
            
        torchaudio.save(output_path, final_mix, sr)
        print(f"--- Pipeline Complete! Master saved to: {output_path} ---")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        pipeline = AIPostProductionPipeline()
        pipeline.process(sys.argv[1])
    else:
        print("Please provide a path to a raw generative audio file.")
