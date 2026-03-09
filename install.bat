@echo off
echo Installing Enhanced JARVIS Voice Assistant...
echo.

echo Checking Python installation...
python --version
if errorlevel 1 (
    echo Python is not installed or not in PATH!
    echo Please install Python 3.7+ from https://python.org
    pause
    exit /b 1
)

echo.
echo Installing required packages...
pip install -r requirements.txt

if errorlevel 1 (
    echo.
    echo Installation failed! Trying alternative methods...
    echo Installing PyAudio separately...
    pip install pipwin
    pipwin install pyaudio
    pip install -r requirements.txt --no-deps
)

echo.
echo Installation complete!
echo.
echo To run Enhanced JARVIS:
echo   python enhanced_main.py
echo.
echo To run original version:
echo   python main.py
echo.
pause
