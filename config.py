# Advanced Configuration for Enhanced JARVIS

# Voice Recognition Settings
RECOGNITION_CONFIG = {
    'energy_threshold': 300,
    'dynamic_energy_threshold': True,
    'dynamic_energy_adjustment_damping': 0.15,
    'dynamic_energy_ratio': 1.5,
    'pause_threshold': 0.8,
    'phrase_threshold': 0.3,
    'non_speaking_duration': 0.5
}

# Text-to-Speech Settings
TTS_CONFIG = {
    'rate': 180,
    'volume': 0.9,
    'voice_index': 0  # 0 for default, 1 for alternative voice
}

# System Settings
SYSTEM_CONFIG = {
    'auto_start': False,
    'hotkey_enabled': True,
    'hotkey': 'ctrl+space',
    'response_delay': 0.5
}

# API Endpoints
API_CONFIG = {
    'weather_base_url': 'http://api.openweathermap.org/data/2.5/weather',
    'news_base_url': 'https://newsapi.org/v2/top-headlines',
    'wikipedia_lang': 'en'
}

# Logging Configuration
LOGGING_CONFIG = {
    'enabled': True,
    'level': 'INFO',
    'log_file': 'jarvis.log',
    'max_log_size': '10MB'
}
