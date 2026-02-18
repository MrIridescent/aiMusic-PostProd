# Infrastructure & Deployment Specifications

## Recommended Environment
This pipeline is computationally intensive and **requires a dedicated GPU environment**.

### Standard Workstation (Local Use)
- **OS**: Linux (Ubuntu 22.04+ recommended) or Windows (via WSL2).
- **GPU**: NVIDIA RTX 3060 (12GB VRAM) or higher. 
  - *Note*: Demucs `htdemucs_ft` requires ~8GB VRAM for stable processing.
- **CPU**: 8-core (AMD Ryzen 7 or Intel i7).
- **RAM**: 16GB+ (32GB preferred for audio chunking).

### Server/Cloud Specs (Scalable Use)
- **Recommended**: AWS `g4dn.xlarge` or RunPod/Lambda Labs with NVIDIA A10G/L4.
- **Backend Deployment**: **Hugging Face Spaces** (with GPU upgrade) is the most turnkey cloud solution for this pipeline.

### Why Netlify for the Front-End?
Netlify will host the **Documentation Hub** and **UI Dashboard**, but it cannot execute the Python pipeline due to 10s timeout limits and lack of GPU. The UI will communicate with a GPU-enabled backend (like a FastAPI server on RunPod).
