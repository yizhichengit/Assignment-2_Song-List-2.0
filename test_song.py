# test_song.py
# (Incomplete) Tests for Song class.
from song import Song

def run_tests():
    """Test Song class."""

    # Test empty song (defaults)
    print("Test empty song:")
    # Create a song with default values
    default_song = Song()
    print(default_song)
    # Check if default values are correctly set
    assert default_song.artist == ""
    assert default_song.title == ""
    assert default_song.year == 0
    assert not default_song.is_learned  # Learned status should be False by default

    # Test initial-value song
    print("\nTest initial-value song:")
    # Create a song with specific values
    initial_song = Song("My Happiness", "Powderfinger", 1996, True)
    print(initial_song)
    # Check if values are correctly assigned
    assert initial_song.artist == "Powderfinger"
    assert initial_song.title == "My Happiness"
    assert initial_song.year == 1996
    assert initial_song.is_learned  # Learned status should be True

    # Test mark_as_learned and mark_as_unlearned methods
    print("\nTest mark_as_learned and mark_as_unlearned methods:")
    # Create a song with initial unlearned status
    unlearned_song = Song("Unlearned Song", "Unknown Artist", 2000)
    print(f"Before learning: {unlearned_song}")
    # Check initial learned status
    assert not unlearned_song.is_learned

    # Test marking the song as learned
    unlearned_song.mark_as_learned()
    print(f"After learning: {unlearned_song}")
    # Check if the song is marked as learned
    assert unlearned_song.is_learned

    # Test marking the song as unlearned
    unlearned_song.mark_as_unlearned()
    print(f"After unlearning: {unlearned_song}")
    # Check if the song is marked as unlearned
    assert not unlearned_song.is_learned

# Run the test cases
run_tests()


