# 🛠️ Operational Manual: Step-by-Step Technical Guide

This guide is designed for both beginners and developers to get the pipeline running in under 5 minutes.

## Step 1: Clone & Navigate
First, get the code on your machine:
```bash
git clone https://github.com/your-username/aiMusic-PostProd.git
cd aiMusic-PostProd
```

## Step 2: Running the Turnkey Wizard 🪄
We have provided a **Setup Wizard** to handle all the complex environment checks, dependency installs, and initial configurations automatically.

```bash
python wizard.py
```
*The wizard will check for Python, FFmpeg, and GPU availability.*

## Step 3: Configure Your AI Conductor (Optional)
If you want to use the **AI-Driven Orchestration**, add your Hugging Face API Token:
1. Open `.env` (created by the wizard).
2. Add your token: `HF_TOKEN=your_hf_token_here`.

## Step 4: Process Your First Track 🚀
Drop an `.mp3` or `.wav` file into the root directory and run:
```bash
python src/main.py my_ai_track.mp3
```
The system will then perform:
1. **Source Separation**: Dismantling the file into stems.
2. **Neural Restoration**: Denoising and high-frequency inpainting.
3. **AI Mixing**: Auto-EQ and compression.
4. **Mastering**: Final export to `output/final_master.wav`.

## Troubleshooting & Tips
- **Low VRAM?** Use `htdemucs_light` instead of `htdemucs_ft` in `src/pipeline/demix.py`.
- **Metallic sound remains?** Increase the `Metallic Artifact Removal` intensity in `src/pipeline/restoration.py`.
