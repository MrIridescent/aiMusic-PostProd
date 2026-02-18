import os
import sys
import subprocess
import platform

def print_banner():
    print("=" * 60)
    print("   🎨 AI Music Post-Prod Pipeline: TURNKEY SETUP WIZARD   ")
    print("=" * 60)
    print("\nStarting environment validation...\n")

def check_python():
    print("[1/4] Checking Python version...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"      ✅ Python {version.major}.{version.minor} found.")
        return True
    else:
        print(f"      ❌ Python 3.8+ required. Found {version.major}.{version.minor}")
        return False

def check_gpu():
    print("[2/4] Checking for NVIDIA GPU...")
    try:
        import torch
        if torch.cuda.is_available():
            print(f"      ✅ NVIDIA GPU found: {torch.cuda.get_device_name(0)}")
            return True
        else:
            print("      ⚠️ No NVIDIA GPU found. System will run on CPU (Slow).")
            return False
    except ImportError:
        print("      ⚠️ PyTorch not yet installed. GPU check deferred.")
        return False

def check_ffmpeg():
    print("[3/4] Checking for FFmpeg (required for .mp3)...")
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print("      ✅ FFmpeg is installed.")
        return True
    except FileNotFoundError:
        print("      ❌ FFmpeg not found! Please install it (e.g., 'sudo apt install ffmpeg').")
        return False

def install_deps():
    print("[4/4] Installing Python dependencies (this may take a few mins)...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("      ✅ All dependencies installed successfully.")
    except Exception as e:
        print(f"      ❌ Dependency installation failed: {e}")

def create_env():
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("# Hugging Face Token for AI Conductor\nHF_TOKEN=your_token_here\n")
        print("      ✅ Created default .env file.")

def main():
    print_banner()
    if not check_python(): return
    check_gpu()
    check_ffmpeg()
    
    confirm = input("\nReady to install dependencies? (y/n): ")
    if confirm.lower() == 'y':
        install_deps()
        create_env()
        print("\n" + "=" * 60)
        print("   🎉 SETUP COMPLETE! You are ready to start mixing.   ")
        print("   Run: python src/main.py path/to/your/audio.mp3      ")
        print("=" * 60)
    else:
        print("\nSetup aborted by user.")

if __name__ == "__main__":
    main()
