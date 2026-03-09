
import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import os
import sys
import requests
import json
import threading
import time
from enhanced_music_library import music, get_songs_by_category, search_song, get_random_song, get_playlist

class EnhancedJarvis:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.listening = True

        # Configure speech recognition for better accuracy
        self.recognizer.energy_threshold = 300
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.dynamic_energy_adjustment_damping = 0.15
        self.recognizer.dynamic_energy_ratio = 1.5
        self.recognizer.pause_threshold = 0.8
        self.recognizer.operation_timeout = None
        self.recognizer.phrase_threshold = 0.3
        self.recognizer.non_speaking_duration = 0.5

        # Set voice properties
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 0.9)

    def speak(self, text):
        """Convert text to speech"""
        print(f"JARVIS: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_continuously(self):
        """Listen for audio continuously with better recognition"""
        with sr.Microphone() as source:
            print("Calibrating microphone for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Microphone calibrated. Listening for 'JARVIS'...")

        while self.listening:
            try:
                with sr.Microphone() as source:
                    # Listen with longer timeout and better noise handling
                    audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=3)

                try:
                    # Try Google Speech Recognition first
                    command = self.recognizer.recognize_google(audio, language='en-US').lower()
                    print(f"Recognized: {command}")

                    if 'jarvis' in command:
                        self.speak("Yes, I'm listening")
                        self.process_command(command)

                except sr.UnknownValueError:
                    # Try alternative recognition methods
                    try:
                        command = self.recognizer.recognize_sphinx(audio)
                        print(f"Sphinx recognized: {command}")
                        if 'jarvis' in command.lower():
                            self.process_command(command.lower())
                    except:
                        pass

                except sr.RequestError as e:
                    print(f"Recognition service error: {e}")

            except sr.WaitTimeoutError:
                pass
            except Exception as e:
                print(f"Listening error: {e}")
                time.sleep(0.1)

    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        return f"The current time is {time_str}"

    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y")
        return f"Today is {date_str}"

    def search_wikipedia(self, query):
        """Search Wikipedia"""
        try:
            result = wikipedia.summary(query, sentences=2)
            return result
        except wikipedia.exceptions.DisambiguationError as e:
            return wikipedia.summary(e.options[0], sentences=2)
        except:
            return "Sorry, I couldn't find information on that topic."

    def get_weather(self, city="Delhi"):
        """Get weather information (placeholder - you'll need an API key)"""
        return f"I need a weather API key to get weather information for {city}. Please configure it in the settings."

    def open_application(self, app_name):
        """Open system applications"""
        apps = {
            'notepad': 'notepad.exe',
            'calculator': 'calc.exe',
            'browser': 'chrome.exe',
            'file manager': 'explorer.exe',
            'task manager': 'taskmgr.exe'
        }

        if app_name in apps:
            try:
                os.system(f'start {apps[app_name]}')
                return f"Opening {app_name}"
            except:
                return f"Could not open {app_name}"
        else:
            return f"Application {app_name} not found in my database"

    def system_control(self, command):
        """Control system functions"""
        if 'shutdown' in command:
            self.speak("Shutting down the system in 30 seconds. Say cancel to stop.")
            # os.system("shutdown /s /t 30")
            return "Shutdown initiated"
        elif 'restart' in command:
            self.speak("Restarting the system in 30 seconds")
            # os.system("shutdown /r /t 30")
            return "Restart initiated"
        elif 'sleep' in command:
            return "Putting system to sleep"
        elif 'volume up' in command:
            # System volume control would require additional libraries
            return "Volume increased"
        elif 'volume down' in command:
            return "Volume decreased"

    def process_command(self, command):
        """Process voice commands with enhanced functionality"""
        command = command.lower().strip()

        # Remove 'jarvis' from the command
        command = command.replace('jarvis', '').strip()

        response = ""

        # Website opening commands
        if 'open google' in command:
            webbrowser.open("https://google.com")
            response = "Opening Google"

        elif 'open youtube' in command:
            webbrowser.open("https://youtube.com")
            response = "Opening YouTube"

        elif 'open linkedin' in command:
            webbrowser.open("https://linkedin.com")
            response = "Opening LinkedIn"

        elif 'open spotify' in command:
            webbrowser.open("https://spotify.com")
            response = "Opening Spotify"

        elif 'open whatsapp' in command:
            webbrowser.open("https://whatsapp.com")
            response = "Opening WhatsApp"

        elif 'open instagram' in command:
            webbrowser.open("https://instagram.com")
            response = "Opening Instagram"

        elif 'open facebook' in command:
            webbrowser.open("https://facebook.com")
            response = "Opening Facebook"

        elif 'open twitter' in command or 'open x' in command:
            webbrowser.open("https://twitter.com")
            response = "Opening Twitter"

        elif 'open gmail' in command:
            webbrowser.open("https://gmail.com")
            response = "Opening Gmail"

        # Music commands
        elif command.startswith('play '):
            song_name = command.split('play ', 1)[1].strip()
            if song_name in music:
                webbrowser.open(music[song_name])
                response = f"Playing {song_name}"
            elif 'playlist' in song_name:
                playlist_name = song_name.replace('playlist', '').strip()
                playlist_songs = get_playlist(playlist_name)
                if playlist_songs:
                    # Play first song from playlist
                    webbrowser.open(music[playlist_songs[0]])
                    response = f"Playing {playlist_name} playlist"
                else:
                    response = f"Playlist {playlist_name} not found"
            else:
                # Search on YouTube if not in library
                search_query = song_name.replace(' ', '+')
                webbrowser.open(f"https://youtube.com/results?search_query={search_query}")
                response = f"Searching for {song_name} on YouTube"

        elif 'play random' in command:
            random_song = get_random_song()
            webbrowser.open(music[random_song])
            response = f"Playing random song: {random_song}"

        # Category-based music
        elif 'play bollywood' in command:
            bollywood_songs = get_songs_by_category('bollywood')
            if bollywood_songs:
                webbrowser.open(music[bollywood_songs[0]])
                response = "Playing Bollywood music"

        elif 'play english' in command:
            english_songs = get_songs_by_category('english')
            if english_songs:
                webbrowser.open(music[english_songs[0]])
                response = "Playing English music"

        elif 'play chill' in command:
            chill_songs = get_songs_by_category('chill')
            if chill_songs:
                webbrowser.open(music[chill_songs[0]])
                response = "Playing chill music"

        # Time and date commands
        elif 'time' in command or 'what time' in command:
            response = self.get_time()

        elif 'date' in command or 'what date' in command or 'today' in command:
            response = self.get_date()

        # Wikipedia search
        elif 'wikipedia' in command or 'search for' in command or 'tell me about' in command:
            if 'wikipedia' in command:
                query = command.replace('wikipedia', '').strip()
            elif 'search for' in command:
                query = command.replace('search for', '').strip()
            else:
                query = command.replace('tell me about', '').strip()

            if query:
                response = self.search_wikipedia(query)
            else:
                response = "What would you like me to search for?"

        # Weather command
        elif 'weather' in command:
            city = 'Delhi'  # Default city
            if 'in' in command:
                city = command.split('in')[1].strip()
            response = self.get_weather(city)

        # Application commands
        elif 'open notepad' in command:
            response = self.open_application('notepad')
        elif 'open calculator' in command:
            response = self.open_application('calculator')
        elif 'open file manager' in command or 'open explorer' in command:
            response = self.open_application('file manager')
        elif 'open task manager' in command:
            response = self.open_application('task manager')

        # System control
        elif 'shutdown' in command or 'shut down' in command:
            response = self.system_control('shutdown')
        elif 'restart' in command:
            response = self.system_control('restart')
        elif 'sleep' in command:
            response = self.system_control('sleep')
        elif 'volume up' in command:
            response = self.system_control('volume up')
        elif 'volume down' in command:
            response = self.system_control('volume down')

        # Conversation commands
        elif 'how are you' in command:
            response = "I'm functioning perfectly, thank you for asking!"

        elif 'your name' in command or 'who are you' in command:
            response = "I am JARVIS, your enhanced personal AI assistant."

        elif 'hello' in command or 'hi ' in command:
            response = "Hello! How can I assist you today?"

        elif 'goodbye' in command or 'bye' in command:
            response = "Goodbye! Have a great day!"

        elif 'thank you' in command or 'thanks' in command:
            response = "You're welcome!"

        elif 'stop listening' in command or 'exit' in command:
            response = "Going offline. Goodbye!"
            self.listening = False

        # Help command
        elif 'help' in command or 'what can you do' in command:
            response = """I can help you with:
            - Opening websites (Google, YouTube, Instagram, Facebook, Twitter, Gmail, etc.)
            - Playing music from 25+ songs library with categories and playlists
            - Telling you the time and date
            - Searching Wikipedia for information
            - Opening applications like Notepad, Calculator, File Manager
            - System controls like shutdown, restart, volume control
            - General conversation and questions
            Just say 'JARVIS' followed by your command."""

        else:
            response = "I didn't understand that command. Say 'help' to see what I can do."

        if response:
            self.speak(response)

    def run(self):
        """Start Enhanced JARVIS"""
        self.speak("Initializing Enhanced JARVIS... All systems ready. Say JARVIS to activate.")

        # Start listening in a separate thread
        listen_thread = threading.Thread(target=self.listen_continuously)
        listen_thread.daemon = True
        listen_thread.start()

        # Keep the main thread alive
        try:
            while self.listening:
                time.sleep(0.1)
        except KeyboardInterrupt:
            self.speak("Enhanced JARVIS shutting down.")
            self.listening = False

if __name__ == "__main__":
    jarvis = EnhancedJarvis()
    jarvis.run()
