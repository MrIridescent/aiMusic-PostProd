# 🎵 AI Music Post-Production Pipeline

[![Live Dashboard](https://img.shields.io/badge/Live-Dashboard-blue)](https://your-netlify-app.netlify.app)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

An **autonomous, studio-grade audio engineering framework** designed to dismantle, restore, and master generative AI music.

## 🌟 Features
- **Turnkey Setup**: Automated wizard for environment configuration.
- **Stage I (Demixing)**: Hybrid transformer source separation (Demucs).
- **Stage II (Restoration)**: Neural denoising (DeepFilterNet) & High-Freq Inpainting (AudioSR).
- **Stage III (Mixing)**: Programmatic DSP engine (Pedalboard) with VST3 support.
- **Stage IV (Conductor)**: Intelligent AI agent (smolagents) for dynamic mixing adjustments.

## 🚀 Quick Start (Noob Friendly)
1. **Clone the Repo**:
   ```bash
   git clone https://github.com/your-username/aiMusic-PostProd.git
   cd aiMusic-PostProd
   ```
2. **Run the Setup Wizard**:
   ```bash
   python wizard.py
   ```
3. **Mix Your First Track**:
   ```bash
   python src/main.py path/to/your/audio.mp3
   ```

## 📚 Documentation
- [Research & Citations](./docs/RESEARCH.md)
- [Operational Manual](./docs/OPERATIONAL.md)
- [Hardware & Server Specs](./docs/HARDWARE.md)
- [Architecture Infographic](./docs/infographic.html)

## 🌐 Netlify Deployment
The `web/` directory is ready for deployment to Netlify. It serves as your project's landing page and documentation hub.

## ⚖️ License
MIT License. Created for the future of autonomous music production.
