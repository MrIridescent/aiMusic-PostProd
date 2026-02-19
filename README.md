# 🎵 AI Music Post-Production Pipeline v1.1.0 (Nuanced)

[![Live Documentation](https://img.shields.io/badge/Live-Documentation-blue)](https://aimusic-postprod.netlify.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![GPU: NVIDIA Required](https://img.shields.io/badge/GPU-NVIDIA%20RTX%203060+-green.svg)](https://developer.nvidia.com/cuda-gpus)

### "Elevating Generative Music from the Uncanny Valley to Studio-Grade Fidelity."

---

## 🏗️ Architectural Overview
This framework is an **autonomous, non-linear audio signal processing (ASP) engine** specifically engineered to remediate the "acoustic pathologies" produced by transformer-based audio synthesis (e.g., Suno, Udio, Stable Audio).

### 🩺 Diagnostic Coverage
Our pipeline systematically addresses:
1.  **Metallic Vocoder Shimmer**: High-frequency ringing (8-12kHz) common in latent diffusion decoders.
2.  **Low-Mid Congestion**: The "boxy" or "muddy" spectral profile (200-500Hz) inherent in over-compressed generative mixes.
3.  **Spectral Holes**: Inpainting missing high-frequency harmonics (16-24kHz) lost during generative bottlenecks.
4.  **Rigid Quantization**: Humanizing AI vocals by injecting 4.5Hz vibrato and noise-shaped masking.

---

## 🚀 One-Click Turnkey Solutions
We believe in **"Noob-Friendly"** engineering. The system is designed to be fully operational with zero manual configuration.

### 🏁 Master Automation (Linux/macOS)
```bash
git clone https://github.com/mriridescent/aiMusic-PostProd.git
cd aiMusic-PostProd
./AUTOMATE.sh your_track.mp3
```
*This script isolates the environment, resolves 100% of dependencies (including Torch, Demucs, and Pedalboard), and executes the pipeline.*

### 🪄 Setup Wizard (Windows/Manual)
```bash
python wizard.py
```
*A self-explaining wizard that validates your GPU (CUDA), FFmpeg installation, and Python environment.*

---

## 🛠️ The 4-Stage Pipeline

### Stage I: High-Fidelity Demixing
- **Engine**: Meta AI's Demucs v4 (`htdemucs_ft`).
- **Metric**: 8.4 dB Signal-to-Distortion Ratio (SDR) for vocal extraction.
- **Nuance**: Hybrid time-frequency processing with 10s chunking/1s crossfade to prevent OOM on 8GB VRAM GPUs.

### Stage II: Neural Audio Restoration
- **Denoising**: `DeepFilterNet3` operating in the ERB domain (0.19 RTF).
- **Super-Resolution**: `AudioSR` latent bridge models to synthesize missing harmonics up to 48kHz.

### Stage III: Programmatic Mixing (DSP)
- **Engine**: Spotify Pedalboard (C++ JUCE wrapper).
- **Performance**: 300x faster than native Python; bypasses GIL for multi-threaded processing.
- **Nuance**: Dynamic EQ carving, 1-3ms lookahead compression, and "Vocal Naturalization".

### Stage IV: AI Agent Conductor (The "Brain")
- **Framework**: `smolagents` (Hugging Face) using a **ReAct (Reason + Act)** loop.
- **Logic**: The agent "listens" to spectral centroid and flatness metrics and autonomously reconfigures the mix parameters until target fidelity is reached.

---

## 🌐 Documentation Hub
For deep-dives into the research and operation of this system, please refer to:
- 📑 **[Granular Technical Specification](./docs/TECHNICAL_SPECIFICATION.md)**
- 🧬 **[Research & Acoustic Pathology](./docs/RESEARCH.md)**
- ⚙️ **[Operational Manual](./docs/OPERATIONAL.md)**
- 📊 **[Interactive Architecture Infographic](./docs/infographic.html)**

---

## 👑 Creator & Branding
**Programmer & Visionary**: [David Akpoviroro Oke](https://github.com/mriridescent)  
**Brand**: **MrIridescent (The Creative Renaissance Man)**  
*Bridging the gap between avant-garde creative expression and high-performance software engineering.*

## ⚖️ License & Acknowledgments
Licensed under **MIT**. Built using Meta AI's Demucs, Spotify's Pedalboard, and Hugging Face's smolagents. 

*Designed for the future of autonomous music production.*
