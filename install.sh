#!/bin/bash

echo "Installing Enhanced JARVIS Voice Assistant..."
echo

# Check Python installation
if ! command -v python3 &> /dev/null; then
    echo "Python 3 is not installed!"
    echo "Please install Python 3.7+ first"
    exit 1
fi

echo "Python version:"
python3 --version
echo

# Install system dependencies for audio
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Installing system dependencies for Ubuntu/Debian..."
    sudo apt-get update
    sudo apt-get install -y python3-pyaudio portaudio19-dev
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Installing system dependencies for macOS..."
    if command -v brew &> /dev/null; then
        brew install portaudio
    else
        echo "Homebrew not found. Please install portaudio manually."
    fi
fi

echo "Installing Python packages..."
pip3 install -r requirements.txt

if [ $? -eq 0 ]; then
    echo
    echo "Installation complete!"
    echo
    echo "To run Enhanced JARVIS:"
    echo "  python3 enhanced_main.py"
    echo
    echo "To run original version:"
    echo "  python3 main.py"
else
    echo "Installation failed! Check error messages above."
    exit 1
fi
