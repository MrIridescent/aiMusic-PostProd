#!/bin/bash

# --- 1-CLICK AUTOMATION SCRIPT ---
# This script sets up the environment and runs the pipeline.

set -e

echo "=========================================================="
echo "   🚀 AI MUSIC POST-PROD: AUTOMATED ONE-CLICK ENGINE"
echo "=========================================================="

# 1. Environment Check
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python 3.8+."
    exit 1
fi

# 2. Virtual Environment Setup
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
fi

source venv/bin/activate

# 3. Dependency Installation
echo "📥 Installing dependencies (Turnkey)..."
pip install --upgrade pip
pip install -r requirements.txt

# 4. Model & Configuration
if [ ! -f ".env" ]; then
    echo "🔧 Creating .env configuration..."
    echo "HF_TOKEN=your_token_here" > .env
fi

# 5. Execution Logic
if [ -z "$1" ]; then
    echo "⚠️ No input file provided."
    echo "Usage: ./AUTOMATE.sh path/to/track.mp3"
    echo "----------------------------------------------------------"
    read -p "Would you like to run a demo with a sample file? (y/n): " DEMO
    if [ "$DEMO" == "y" ]; then
        echo "🏃 Running Pipeline Demo..."
        # In a real scenario, we'd provide a sample.mp3
        python3 src/main.py sample.mp3 || echo "ℹ️ Sample run failed (No sample.mp3 found)."
    fi
else
    python3 src/main.py "$1"
fi

echo "=========================================================="
echo "   🎉 DONE! Check the 'output/' directory for results."
echo "=========================================================="
