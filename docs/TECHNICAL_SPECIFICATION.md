# AI Music Post-Production Pipeline: Technical Specification & Deep-Dive
**Version**: 1.0.0 (Turnkey Edition)  
**Last Updated**: February 18, 2026

## 1. Executive Summary
This framework is an autonomous, non-linear audio signal processing (ASP) engine designed specifically for generative AI music. It addresses artifacts produced by **Transformer-based audio synthesis** and **latent diffusion decoders**.

## 2. Architectural Stages (Deep-Dive)

### Stage I: Source Separation (Demultiplexing)
- **Model**: Meta AI's Demucs v4 (Hybrid Transformer).
- **Nuance**: The system uses `htdemucs_ft` with a 2-second overlapping chunking strategy. This preserves phase coherence in the time domain while utilizing spectral frequency masks for cleaner vocal extraction.
- **Why?**: Generative models bake audio into a single stereo file. Separating stems is the **only way** to apply restorative EQ without destructive interference.

### Stage II: Neural Restoration
- **Denoising**: Uses **DeepFilterNet**, a complex-valued neural network operating in the Equivalent Rectangular Bandwidth (ERB) domain. It targets non-stationary artifacts (metallic shimmer) that traditional spectral gates cannot isolate.
- **Inpainting (AudioSR)**: Utilizes latent diffusion to hallucinate missing high-frequency harmonics (16kHz-24kHz). This restores the "brilliance" lost during the generative synthesis bottleneck.

### Stage III: Programmatic Mixing (DSP Engine)
- **Engine**: Spotify Pedalboard (C++ JUCE wrapper).
- **Nuance**: Bypasses Python's Global Interpreter Lock (GIL) to process audio 300x faster than traditional Python loops. Supports native VST3 integration, allowing professional-grade analog modeling within a headless script.

### Stage IV: AI Conductor (ReAct Orchestrator)
- **Framework**: smolagents.
- **Operation**: The Conductor LLM (Llama-3-70B) runs a feedback loop:
  1. **Measure**: Extract spectral centroid and flatness.
  2. **Act**: Adjust EQ/Compressor parameters via tool calls.
  3. **Verify**: Re-analyze until the "muddy" or "harsh" profile is resolved.

## 3. Operational Use Cases
### Case 3.1: Professional Producer (Real-World)
A producer uses Suno for melody ideation but needs the stems to be radio-ready. They run the pipeline to extract a clean dry vocal and a punchy drum transient, which they then pull into a DAW like Ableton Live.

### Case 3.2: Content Creator (Turnkey)
A YouTuber generates background music via Udio. They use the **1-Click AUTOMATE.sh** to ensure the background track doesn't clash with their voice-over, as the system automatically carves out the mid-range (200-500Hz).

## 4. Hardware & Scaling Recommendations
- **Edge Deployment**: For real-time use, utilize `htdemucs_light` on a Jetson Orin Nano.
- **Enterprise Scaling**: Deploy as a microservice on AWS g4dn instances, using FastAPI to bridge the Python pipeline to a web front-end.
