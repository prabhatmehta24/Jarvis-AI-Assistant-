# Enhanced JARVIS Voice Assistant - Complete Setup Guide

## 🚀 Project Overview

Enhanced JARVIS is an advanced voice-controlled personal assistant inspired by Iron Man's AI assistant. It features comprehensive voice recognition, music playback, web automation, system control, and an intuitive web-based UI.

## 📋 Features

### Core Functionality
- **Advanced Voice Recognition** with multiple fallback engines
- **25+ Song Music Library** with category-based organization
- **Website Automation** (Google, YouTube, Instagram, LinkedIn, etc.)
- **System Control** (Applications, shutdown, restart, volume)
- **Information Queries** (Time, date, Wikipedia, weather)
- **Smart Conversations** with context awareness

### Enhanced Audio Recognition
- Continuous listening with noise filtering
- Multiple recognition engines (Google + Sphinx)
- Adjustable sensitivity and energy thresholds
- Better handling of different accents and speech patterns
- Real-time microphone calibration

### Music Library Features
- **Categories**: Bollywood, English, Chill, Rock, Electronic, Original
- **Playlists**: Favorites, Workout, Relax, Party
- **25+ Songs** including popular hits and classics
- **Smart Search** and random song selection

## 🛠️ Installation Instructions

### Prerequisites
- Python 3.7 or higher
- Working microphone
- Internet connection
- Web browser

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install PyAudio (Critical for microphone input)

#### For Windows:
```bash
pip install pyaudio
```
If this fails, try:
```bash
pip install pipwin
pipwin install pyaudio
```

#### For macOS:
```bash
brew install portaudio
pip install pyaudio
```

#### For Ubuntu/Linux:
```bash
sudo apt-get install python3-pyaudio
pip install pyaudio
```

### Step 3: Install Additional Dependencies (Optional)
For better speech recognition accuracy:
```bash
pip install pocketsphinx
```

### Step 4: Test Installation
Run this command to test speech recognition:
```bash
python -m speech_recognition
```

## 🎯 Running JARVIS

### Method 1: Enhanced Version (Recommended)
```bash
python enhanced_main.py
```

### Method 2: Original Version
```bash
python main.py
```

### Method 3: Web UI
Open the HTML file in your browser for the web interface.

## 🎤 Voice Commands Guide

### Wake Word
Always start with **"JARVIS"** followed by your command.

### Website Navigation
- "JARVIS, open Google"
- "JARVIS, open YouTube"
- "JARVIS, open Instagram"
- "JARVIS, open LinkedIn"
- "JARVIS, open Spotify"
- "JARVIS, open WhatsApp"
- "JARVIS, open Facebook"
- "JARVIS, open Twitter"
- "JARVIS, open Gmail"

### Music Control
- "JARVIS, play Kesariya"
- "JARVIS, play Shape of You"
- "JARVIS, play Bollywood songs"
- "JARVIS, play chill music"
- "JARVIS, play random song"
- "JARVIS, play favorites playlist"
- "JARVIS, play workout playlist"

### Information Queries
- "JARVIS, what time is it?"
- "JARVIS, what date is it?"
- "JARVIS, search for artificial intelligence"
- "JARVIS, tell me about machine learning"
- "JARVIS, weather in Delhi"

### System Control
- "JARVIS, open Notepad"
- "JARVIS, open Calculator"
- "JARVIS, open File Manager"
- "JARVIS, open Task Manager"
- "JARVIS, shutdown"
- "JARVIS, restart"
- "JARVIS, volume up"
- "JARVIS, volume down"

### Conversation
- "JARVIS, hello"
- "JARVIS, how are you?"
- "JARVIS, who are you?"
- "JARVIS, help"
- "JARVIS, thank you"
- "JARVIS, goodbye"
- "JARVIS, stop listening"

## 🎵 Music Library

### Categories Available:
1. **Bollywood**: Kesariya, Apna Bana Le, Dil Bechara, Tum Hi Aana, Raabta, Aaj Se Teri
2. **English**: Shape of You, Perfect, Despacito, Someone Like You, Hello
3. **Chill**: Lofi Hip Hop, Chill Music, Study Music, Natural
4. **Rock**: Bohemian Rhapsody, Imagine, Hotel California
5. **Electronic**: Closer, Faded, Alone
6. **Original**: Stealth, Natural, Festival, Monks, Aaj Se Teri

### Playlists Available:
- **Favorites**: Top picks across genres
- **Workout**: High-energy electronic music
- **Relax**: Chill and ambient tracks
- **Party**: Upbeat popular songs

## 🔧 Troubleshooting

### Common Issues and Solutions:

#### 1. Microphone Not Working
- Check microphone permissions in system settings
- Test with: `python -m speech_recognition`
- Try adjusting microphone position
- Reduce background noise

#### 2. PyAudio Installation Fails
- Install Visual C++ Build Tools (Windows)
- Use conda instead: `conda install pyaudio`
- Try alternative: `pip install pipwin` then `pipwin install pyaudio`

#### 3. Low Speech Recognition Accuracy
- Speak clearly and at normal pace
- Position microphone 6-12 inches from mouth
- Minimize background noise
- Use the wake word "JARVIS" before each command
- Wait for audio confirmation before next command

#### 4. Import Errors
- Ensure all requirements are installed: `pip install -r requirements.txt`
- Check Python version (3.7+ recommended)
- Try creating a virtual environment

#### 5. Web Browser Not Opening
- Check default browser settings
- Ensure internet connection is active
- Try manually opening one website to test

### Performance Optimization Tips:
- Use a good quality USB microphone
- Close unnecessary applications
- Ensure stable internet connection
- Run in a quiet environment
- Update Python to latest version

## 🎨 Customization

### Adding New Songs
Edit `enhanced_music_library.py`:
```python
music["your song name"] = "youtube_url_here"
```

### Adding New Voice Commands
Edit the `process_command` method in `enhanced_main.py` to add custom commands.

### Changing Voice Settings
Modify voice properties in the `__init__` method:
```python
self.engine.setProperty('rate', 180)    # Speaking rate
self.engine.setProperty('volume', 0.9)  # Volume level
```

### Creating Custom Playlists
Add to `enhanced_music_library.py`:
```python
playlists["your_playlist"] = ["song1", "song2", "song3"]
```

## 📁 Project Structure
```
enhanced-jarvis/
├── enhanced_main.py          # Main enhanced JARVIS application
├── enhanced_music_library.py # Comprehensive music database
├── main.py                   # Original JARVIS version
├── music_library.py          # Original music library
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
├── index.html               # Web UI interface
├── style.css                # Web UI styling
├── app.js                   # Web UI functionality
└── SETUP_GUIDE.md           # Detailed setup instructions
```

## 🌐 Web Interface

The project includes a modern web-based control panel with:
- Real-time voice recognition display
- Audio visualizer
- Music library browser
- System status monitoring
- Settings panel
- Command history

Open `index.html` in your browser to access the web interface.

## 🔐 API Keys Setup (Optional)

Create a `.env` file for additional features:
```
WEATHER_API_KEY=your_openweathermap_api_key
NEWS_API_KEY=your_news_api_key
```

## 📞 Support

If you encounter issues:
1. Check this troubleshooting guide
2. Ensure all dependencies are installed correctly
3. Test with the simple commands first
4. Check microphone permissions and settings

## 🚀 Advanced Features

### Multiple Recognition Engines
The enhanced version uses both Google Speech Recognition and PocketSphinx for better accuracy and offline capability.

### Smart Response System
JARVIS now provides contextual responses and can handle variations in command phrasing.

### Enhanced Music Management
- Category-based music organization
- Playlist support with custom playlists
- Search functionality across the music library
- Random song selection

### System Integration
- Application launching and management
- System control (shutdown, restart, volume)
- File operations and process management

## 🎯 Tips for Best Experience

1. **Speak Clearly**: Use normal speaking pace and clear pronunciation
2. **Use Wake Word**: Always say "JARVIS" before your command
3. **Wait for Response**: Allow JARVIS to respond before giving next command
4. **Quiet Environment**: Minimize background noise for better recognition
5. **Good Microphone**: Use a quality microphone for best results

## 📈 Future Enhancements

Planned features for future versions:
- Natural Language Processing for better command understanding
- Integration with more streaming services
- Home automation control
- Calendar and reminder management
- Email integration
- Multi-language support

---

**Enhanced JARVIS** - Your Advanced Personal AI Assistant
