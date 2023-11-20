"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to
"""
Name:Yizhi Chen
Date started:21/10/2023
GitHub URL: https://github.com/yizhichengit/Assignment-2_Song-List-2.0/blob/master/a1_classes.py
"""


from song import Song
from songcollection import SongCollection
import json

# Load Song
def load_songs(filename):
    song_collection = SongCollection()
    with open(filename, 'r') as file:
        songs_data = json.load(file)
        for song_data in songs_data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
            song_collection.add_song(song)
    return song_collection

# Display song list
def display_songs(song_collection):
    songs = song_collection.songs
    for i, song in enumerate(songs, 1):
        learned_status = 'learned' if song.is_learned else 'not learned'
        print(f"{i}. {song.title} by {song.artist} {song.year} ({learned_status})")

# add new songs
def add_new_song(song_collection):
    title = input("Title: ")
    artist = input("Artist: ")
    year = int(input("Year: "))  # Assuming that the year input is always a valid integer here
    song_collection.add_song(Song(title, artist, year))

# Change the learning status of the song
def learn_song(song_collection):
    display_songs(song_collection)
    song_number = int(input("Enter the number of the song to mark as learned: "))
    song_to_learn = song_collection.songs[song_number - 1]
    song_to_learn.is_learned = True
    print(f"You have learned {song_to_learn.title}")

# Save Song to File
def save_songs(song_collection, filename):
    songs_data = []
    for song in song_collection.songs:
        songs_data.append(song.to_dict())  # Assuming the Song class has a to_ dict method
    with open(filename, 'w') as file:
        json.dump(songs_data, file, indent=4)

# main function
def main():
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

# Display menu
def print_menu():
    print("Menu:")
    print("D - Display songs")
    print("A - Add a song")
    print("L - Learn a song")
    print("Q - Quit")

if __name__ == "__main__":
    main()

