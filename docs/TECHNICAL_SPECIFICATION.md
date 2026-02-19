# AI Music Post-Production Pipeline: Granular Technical Specification
**Version**: 1.1.0 (Nuanced Edition)  
**Last Updated**: February 19, 2026

## 1. Executive Summary
This framework addresses the "acoustic pathology" of transformer-based audio synthesis (Suno, Udio, Stable Audio). While generative models offer revolutionary compositional democracy, their raw outputs (flattened, compressed stereo) suffer from spectral holes, 8-12kHz metallic shimmer, and severe frequency masking (200-500Hz).

## 2. Granular Architectural Stages

### Stage I: High-Fidelity Source Separation (Demultiplexing)
- **Primary Model**: Meta AI's Demucs v4 (`htdemucs_ft`).
- **Architecture**: Hybrid transformer architecture processing audio in both time and frequency domains simultaneously.
- **Metric (SDR)**: Signal-to-Distortion Ratio of 8.4 dB for vocals (surpassing Spleeter's 6.2 dB).
- **Nuance**: Preserves phase coherence by operating heavily in the time domain with bidirectional Long Short-Term Memory (BiLSTM) and U-Net structures.
- **Memory Management**: Employs a 10s chunking and 1s linear crossfade overlapping strategy to prevent OOM (Out-Of-Memory) exceptions on consumer GPUs while maintaining seamless reconstruction.

### Stage II: Neural Restoration & Super-Resolution
- **Denoising (DeepFilterNet3)**:
  - **Logic**: Perceptually motivated multi-frame complex filtering in the frequency domain combined with coarse-resolution gain estimation in the Equivalent Rectangular Bandwidth (ERB) domain.
  - **Latency**: Real-time factor (RTF) of 0.19 on standard CPUs.
  - **Target**: Eliminates "musical noise" and underwater artifacts inherent in latent diffusion synthesis.
- **Bandwidth Extension (AudioSR)**:
  - **Logic**: Latent Bridge Model (LBM) maps low-res latent vectors to high-res.
  - **Target**: Synthesizes missing 16kHz - 24kHz harmonics to achieve studio-standard 48kHz fidelity.
  - **Nuance**: Requires a strict 16kHz low-pass filter prior to inference to normalize the cutoff pattern for optimal diffusion inpainting.

### Stage III: Programmatic Mixing Engine
- **Framework**: Spotify Pedalboard (C++ JUCE wrapper).
- **Performance**: Bypasses Python's GIL, running up to 300x faster than native Python loops or pySoX.
- **Vocal Naturalization Logic**:
  - **Vibrato Injection**: Subtle 4.5Hz vibrato calculation to break rigid pitch quantization.
  - **Quantization Masking**: Low-amplitude shaped noise (1-4kHz range) to mask "stair-step" artifacts.
  - **Metallic Artifact Removal**: Strict 30% reduction targeted at the 6-10kHz "shimmer" range.
- **Dynamics Chain**: RoughRider 3 analog-modeled compressor with 1-3ms lookahead attack for transient shaping.

### Stage IV: AI Conductor Agent
- **Framework**: smolagents (Hugging Face) using a ReAct (Reason + Act) loop.
- **Tools**: `analyze_nuance` (Spectral Centroid, Flatness, RMS) and `adjust_mixing_parameter`.
- **Logic**: The agent analyzes if the mix is "muddy" (centroid < 1500Hz) or "harsh" (centroid > 4000Hz) and autonomously re-configures the Pedalboard signal chain.

## 3. Recommended Infrastructure
- **GPU**: NVIDIA RTX 3060 (12GB VRAM) minimum for `htdemucs_ft`.
- **Cloud**: AWS `g4dn.xlarge` or RunPod with NVIDIA A10G/L4.
- **Environment**: Linux (Ubuntu 22.04+) with CUDA 11.8+ and FFmpeg (required for mp3 decoding).
