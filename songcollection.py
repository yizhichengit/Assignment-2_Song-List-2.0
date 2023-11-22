"""SongCollection Class."""

import json
from song import Song

class SongCollection:
    def __init__(self):
        """
        Constructor for the SongCollection class.
        Initializes an empty list of songs.
        """
        self.songs = []  # Initialize an empty list to store songs.

    def add_song(self, song):
        """
        Add a single Song object to the song list.

        :param song: Song - The song object to add to the collection.
        """
        self.songs.append(song)  # Add the provided song to the songs list.

    def get_number_of_unlearned_songs(self):
        """
        Get the number of unlearned songs in the collection.

        :return: int - The count of songs that have not been learned.
        """
        # Count and return the number of unlearned songs.
        return sum(not song.is_learned for song in self.songs)

    def get_number_of_learned_songs(self):
        """
        Get the number of learned songs in the collection.

        :return: int - The count of songs that have been learned.
        """
        # Count and return the number of learned songs.
        return sum(song.is_learned for song in self.songs)

    def load_songs(self, filename):
        """
        Load songs from a JSON file into the list of Song objects.

        :param filename: str - The file path to load songs from.
        """
        with open(filename, 'r') as file:
            songs_data = json.load(file)
            for song_data in songs_data:
                # Create a Song object from each dictionary in the JSON file.
                song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
                self.songs.append(song)  # Add the song to the collection.

    def save_songs(self, filename):
        """
        Save songs from the song list into a JSON file.

        :param filename: str - The file path to save songs to.
        """
        songs_data = [song.to_dict() for song in self.songs]  # Convert each song to a dictionary.
        with open(filename, 'w') as file:
            json.dump(songs_data, file, indent=2)  # Write the song data to the file in JSON format.

    def sort(self, key):
        """
        Sort songs by the key passed in, then by title.

        :param key: str - The attribute of Song to sort by.
        """
        # Sort the songs list based on the specified key and then by title.
        self.songs.sort(key=lambda song: (getattr(song, key), song.title))

    def __str__(self):
        """
        String representation of the SongCollection object.

        :return: str - A formatted string of all songs in the collection.
        """
        # Join and return all songs in the collection as a formatted string.
        return "\n".join(str(song) for song in self.songs)


