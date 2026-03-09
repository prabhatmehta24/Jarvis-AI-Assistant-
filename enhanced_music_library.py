
# Enhanced Music Library for JARVIS
# This file contains a comprehensive music database with various genres

music = {
    # Original songs
    "stealth": "https://www.youtube.com/watch?v=yDcrlRny5kA&list=PLqDyiQp0DOxCZ7GFMcKgTN5E_4NrLTCxi",
    "natural": "https://www.youtube.com/watch?v=EjZJdw9gJ9g&list=PLqDyiQp0DOxCZ7GFMcKgTN5E_4NrLTCxi&index=2",
    "festival": "https://www.youtube.com/watch?v=vodU3w9jTVU&list=PLqDyiQp0DOxCZ7GFMcKgTN5E_4NrLTCxi&index=4",
    "monks": "https://www.youtube.com/watch?v=Rfof1k7H1AY&list=PLqDyiQp0DOxCZ7GFMcKgTN5E_4NrLTCxi&index=12",
    "aaj se teri": "https://www.youtube.com/watch?v=NFsEqOBG51M",

    # Popular Bollywood songs
    "kesariya": "https://www.youtube.com/watch?v=BddP6PYo2gs",
    "apna bana le": "https://www.youtube.com/watch?v=5wtUKJ3qABU",
    "dil bechara": "https://www.youtube.com/watch?v=6wMNHJUUaCM",
    "tum hi aana": "https://www.youtube.com/watch?v=wvpaTdkCQHw",
    "raabta": "https://www.youtube.com/watch?v=dW_VZJF8FmE",

    # Popular English songs
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "perfect": "https://www.youtube.com/watch?v=2Vv-BfVoq4g",
    "despacito": "https://www.youtube.com/watch?v=kJQP7kiw5Fk",
    "someone like you": "https://www.youtube.com/watch?v=hLQl3WQQoQ0",
    "hello": "https://www.youtube.com/watch?v=YQHsXMglC9A",

    # Chill/Lofi music
    "lofi hip hop": "https://www.youtube.com/watch?v=jfKfPfyJRdk",
    "chill music": "https://www.youtube.com/watch?v=5qap5aO4i9A",
    "study music": "https://www.youtube.com/watch?v=lTRiuFIWV54",

    # Classic rock
    "bohemian rhapsody": "https://www.youtube.com/watch?v=fJ9rUzIMcZQ",
    "imagine": "https://www.youtube.com/watch?v=YkgkThdzX-8",
    "hotel california": "https://www.youtube.com/watch?v=09839DpTctU",

    # Electronic/Dance
    "closer": "https://www.youtube.com/watch?v=PT2_F-1esPk",
    "faded": "https://www.youtube.com/watch?v=60ItHLz5WEA",
    "alone": "https://www.youtube.com/watch?v=1-xGerv5FOk",
}

# Music categories for better organization
music_categories = {
    "bollywood": ["kesariya", "apna bana le", "dil bechara", "tum hi aana", "raabta", "aaj se teri"],
    "english": ["shape of you", "perfect", "despacito", "someone like you", "hello"],
    "chill": ["lofi hip hop", "chill music", "study music", "natural"],
    "rock": ["bohemian rhapsody", "imagine", "hotel california"],
    "electronic": ["closer", "faded", "alone"],
    "original": ["stealth", "natural", "festival", "monks", "aaj se teri"]
}

def get_songs_by_category(category):
    """Return songs from a specific category"""
    if category.lower() in music_categories:
        return music_categories[category.lower()]
    return []

def search_song(query):
    """Search for songs containing the query"""
    query = query.lower()
    matching_songs = []
    for song in music.keys():
        if query in song.lower():
            matching_songs.append(song)
    return matching_songs

def get_random_song():
    """Get a random song from the library"""
    import random
    return random.choice(list(music.keys()))

def get_all_songs():
    """Return all available songs"""
    return list(music.keys())

# Playlist functionality
playlists = {
    "favorites": ["kesariya", "shape of you", "natural", "bohemian rhapsody"],
    "workout": ["closer", "faded", "alone"],
    "relax": ["lofi hip hop", "chill music", "study music", "natural"],
    "party": ["despacito", "shape of you", "closer", "apna bana le"]
}

def get_playlist(playlist_name):
    """Get songs from a playlist"""
    if playlist_name.lower() in playlists:
        return playlists[playlist_name.lower()]
    return []

def create_playlist(name, songs):
    """Create a new playlist"""
    playlists[name.lower()] = songs
    return f"Playlist '{name}' created with {len(songs)} songs"

def add_to_playlist(playlist_name, song):
    """Add a song to existing playlist"""
    if playlist_name.lower() in playlists and song in music:
        playlists[playlist_name.lower()].append(song)
        return f"Added '{song}' to playlist '{playlist_name}'"
    return "Playlist or song not found"
