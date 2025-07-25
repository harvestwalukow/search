import requests
import sys
from prettytable import PrettyTable


def main():    
    artist_name = get_artist()
    if not artist_name:
        pass
        
    songs = search_songs(artist_name)
    
    if songs:
        display_songs(songs, artist_name)
    else:
        print(f"No songs found for {artist_name}")


def get_artist():
    artist_name = input("Artist name: ").strip()
        
    return artist_name


def search_songs(artist_name):
    try:
        base_url = "https://itunes.apple.com/search"
        params = {
            'term': artist_name,
            'entity': 'song',
            'media': 'music',
            'limit': 50  
        }
                
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        songs = []
        for item in data.get('results', []):
            if item.get('kind') == 'song':
                song_info = {
                    'track_name': item.get('trackName', 'Unknown Track'),
                    'album_name': item.get('collectionName', 'Unknown Album'),
                    'release_date': item.get('releaseDate', 'Unknown')[:10] if item.get('releaseDate') else 'Unknown',
                }
                songs.append(song_info)
        
        return songs
        
    except Exception as e:
        print(f"Search error: {e}")
        return []


def display_songs(songs, artist_name):    
    print(f"\n{len(songs)} songs by '{artist_name}':")
    
    table = PrettyTable()
    table.field_names = ["No.", "Track", "Album", "Released"]
    table.align["Track"] = "l" 
    table.align["Album"] = "l"
    table.max_width["Track"] = 40
    table.max_width["Album"] = 40
    
    for i, song in enumerate(songs, 1):
        table.add_row([
            f"{i}.",
            song['track_name'],
            song['album_name'],
            song['release_date']
        ])
    
    print(table)

if __name__ == "__main__":
    main()