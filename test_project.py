import pytest
from project import get_artist, search_songs, display_songs


def test_get_artist():

    pass


def test_search_songs():
    result = search_songs("d4vd")
    assert isinstance(result, list)
    
    result = search_songs("")
    assert isinstance(result, list)


def test_display_songs():
    sample_songs = [
        {
            'track_name': 'Test Song',
            'album_name': 'Test Album', 
            'release_date': '2023-01-01'
        }
    ]
    
    display_songs(sample_songs, "Test Artist")
    
    display_songs([], "Test Artist")
