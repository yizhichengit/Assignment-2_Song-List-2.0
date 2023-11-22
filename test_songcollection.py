"""(Incomplete) Tests for SongCollection class."""
from song import Song
from songcollection import SongCollection

def run_tests():
    """Test SongCollection class."""

    # Test empty SongCollection (defaults)
    print("Test empty SongCollection:")
    # Create an empty SongCollection
    song_collection = SongCollection()
    print(song_collection)
    # Assert that the song list is initially empty
    assert not song_collection.songs  # an empty list is considered False

    # Test loading songs from a file
    print("Test loading songs:")
    song_collection.load_songs('songs.json')
    print(song_collection)
    # Assert that songs are loaded (assuming 'songs.json' is non-empty)
    assert song_collection.songs  # non-empty list is considered True

    # Test adding a new Song with values
    print("Test adding new song:")
    song_collection.add_song(Song("My Happiness", "Powderfinger", 1996, True))
    print(song_collection)
    # No specific assert here, but check console output for correctness

    # Test sorting songs by year
    print("Test sorting - year:")
    song_collection.sort("year")
    print(song_collection)
    # TODO: Add more specific asserts for sorting tests

    # Test sorting songs by artist
    print("Test sorting - artist:")
    song_collection.sort("artist")
    print(song_collection)
    # TODO: Add more specific asserts for sorting tests

    # Test sorting songs by title
    print("Test sorting - title:")
    song_collection.sort("title")
    print(song_collection)
    # TODO: Add more specific asserts for sorting tests

    # Test saving songs to a file
    print("Test saving songs:")
    song_collection.save_songs('songs.json')
    # Manual check: Open 'songs.json' to see if the results are as expected
    # TODO: Implement a way to automate this test

# Run the test cases
run_tests()

