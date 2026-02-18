# AI Music Post-Production Pipeline

## Build and Environment Setup
The project requires Python 3.8+ and a CUDA-enabled GPU for optimal performance.

### Install Dependencies

Note: To decode `.mp3` files, you must have `ffmpeg` installed on your system.
```bash
pip install -r requirements.txt
```

### Dependencies List
- `torch`, `torchaudio`: Core deep learning and audio processing.
- `demucs`: Source separation (Stage I).
- `df-net`: Neural denoising (DeepFilterNet).
- `pedalboard`: Programmatic mixing engine (Stage III).
- `smolagents`: AI Conductor orchestration (Stage IV).
- `librosa`, `scipy`, `numpy`: Audio analysis and signal processing.

## Running the Pipeline
To process a raw generative audio file:
```bash
python3 src/main.py path/to/audio_file.wav
```

## Testing
Run unit tests for restoration and mixing modules:
```bash
python3 -m unittest tests/test_pipeline.py
```

## Linting
Recommended linting (not installed by default):
```bash
flake8 src
```
