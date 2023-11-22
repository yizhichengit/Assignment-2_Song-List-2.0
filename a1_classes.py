"""
Song List Manager.

This script allows the user to manage a list of songs, including displaying,
adding, and marking songs as learned. The songs are stored in a JSON file.
and Very good use of song class and songcollection class.

Name: Yizhi Chen
Date started: 21/10/2023
GitHub URL: https://github.com/yizhichengit/Assignment-2_Song-List-2.0/blob/master/a1_classes.py
"""

from song import Song
from songcollection import SongCollection
import json


def load_songs(filename):
    """
    Load songs from a JSON file and return a SongCollection object.

    :param filename: str - The name of the file to load songs from.
    :return: SongCollection - The collection of songs.
    """
    song_collection = SongCollection()
    with open(filename, 'r') as file:
        songs_data = json.load(file)
        for song_data in songs_data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
            song_collection.add_song(song)
    return song_collection


def display_songs(song_collection):
    """
    Display all songs in the collection with their number, title, artist, year, and learned status.

    :param song_collection: SongCollection - The collection of songs to display.
    """
    songs = song_collection.songs
    for i, song in enumerate(songs, 1):
        learned_status = 'learned' if song.is_learned else 'not learned'
        print(f"{i}. {song.title} by {song.artist} {song.year} ({learned_status})")


def add_new_song(song_collection):
    """
    Prompt the user to add a new song to the collection.

    :param song_collection: SongCollection - The collection to add a new song to.
    """
    title = input("Title: ")
    artist = input("Artist: ")
    year = int(input("Year: "))  # Assuming that the year input is always a valid integer here
    song_collection.add_song(Song(title, artist, year))


def learn_song(song_collection):
    """
    Mark a song as learned based on user input.

    :param song_collection: SongCollection - The collection of songs to update.
    """
    display_songs(song_collection)
    song_number = int(input("Enter the number of the song to mark as learned: "))
    song_to_learn = song_collection.songs[song_number - 1]
    song_to_learn.is_learned = True
    print(f"You have learned {song_to_learn.title}")


def save_songs(song_collection, filename):
    """
    Save the songs in the collection to a JSON file.

    :param song_collection: SongCollection - The collection of songs to save.
    :param filename: str - The name of the file to save songs to.
    """
    songs_data = [song.to_dict() for song in song_collection.songs]  # Assumes the Song class has a to_dict method
    with open(filename, 'w') as file:
        json.dump(songs_data, file, indent=4)


def main():
    """
    Main function to run the song list manager.
    """
    song_collection = load_songs("songs.json")
    while True:
        print_menu()
        choice = input(">>> ").upper()
        if choice == "Q":
            save_songs(song_collection, "songs.json")
            break
        elif choice == "D":
            display_songs(song_collection)
        elif choice == "A":
            add_new_song(song_collection)
        elif choice == "L":
            learn_song(song_collection)
        else:
            print("Invalid option")


def print_menu():
    """
    Print the main menu options to the console.
    """
    print("Menu:")
    print("D - Display songs")
    print("A - Add a song")
    print("L - Learn a song")
    print("Q - Quit")


if __name__ == "__main__":
    main()
