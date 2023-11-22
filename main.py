"""
Name:Yizhi Chen
Date Started:19/11/2023
Brief Project Description:
This project is a Kivy framework Python application for managing song collections.
It allows users to view a list of songs, add new songs, mark them as learned, and sort them by different criteria.
All song data is stored in JSON files, ensuring data persistence.
The interface includes a scrollable list of songs and user interaction controls, such as input boxes and buttons.
Through this application, users can easily manage and track their music learning progress.

GitHub URL:https://github.com/yizhichengit/Assignment-2_Song-List-2.0/blob/master/main.py
"""
# TODO: Create your main program in this file, using the SongListApp class

# main.py
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from song import Song
from songcollection import SongCollection
import json

# Define the main application class, which inherits from Kivy's App class.
class SongListApp(App):
    # Properties that will update the UI automatically when their values change.
    status_text = StringProperty('')
    song_collection = ObjectProperty(SongCollection())
    learned = NumericProperty(0)
    to_learn = NumericProperty(0)

    # Build the application's UI from the KV file and load songs from the JSON file.
    def build(self):
        self.song_collection = SongCollection()
        self.song_collection.load_songs('songs.json')
        return Builder.load_file('app.kv')

    # Load song data from a given filename and update the song list.
    def load_songs(self, filename):
        self.song_collection.load_songs(filename)
        self.update_song_list()

    # Update the visible list of songs in the UI.
    def update_song_list(self):
        # Clear the current list of song widgets.
        if self.root and hasattr(self.root.ids, 'songs_box'):
            self.root.ids.songs_box.clear_widgets()
        # Create and add a button for each song to the song box.
        for song in self.song_collection.songs:
            button_color = (0, 1, 0, 1) if song.is_learned else (1, 0, 0, 1)
            button = Button(text=f'{song.title} by {song.artist} ({song.year})',
                            background_color=button_color,
                            on_release=self.toggle_learned)
            button.song = song  # Attach the song object to the button for easy access.
            self.root.ids.songs_box.add_widget(button)
        # Update the status labels for learned and to-learn counts.
        self.update_status_text()

    # Add a new song to the collection with data from the input fields.
    def add_song(self):
        title = self.root.ids.title_input.text
        artist = self.root.ids.artist_input.text
        year_text = self.root.ids.year_input.text

        # Validate input fields are not empty.
        if not title or not artist or not year_text:
            self.status_text = "All fields must be completed"
            return

        # Validate year input is a positive integer.
        try:
            year = int(year_text)
            if year <= 0:
                self.status_text = "Year must be > 0"
                return
        except ValueError:
            self.status_text = "Please enter a valid number"
            return

        # Add the new song and clear the input fields.
        self.song_collection.add_song(Song(title, artist, year))
        self.update_song_list()
        self.clear_inputs()

    # Clear the text inputs and reset the status text.
    def clear_inputs(self):
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.status_text = ""

    # Toggle the learned status of a song when its button is pressed.
    def toggle_learned(self, button_instance):
        song = button_instance.song
        song.is_learned = not song.is_learned
        self.update_song_list()  # Refresh the list to reflect the change.

    # Update the learned and to-learn counts based on the song collection.
    def update_status_text(self):
        self.learned = self.song_collection.get_number_of_learned_songs()
        self.to_learn = self.song_collection.get_number_of_unlearned_songs()

    # Save the current list of songs to a JSON file when the app is closing.
    def on_stop(self):
        self.save_songs('songs.json')

    # Write the song collection to a JSON file, converting each song to a dictionary.
    def save_songs(self, filename):
        with open(filename, 'w') as file:
            json.dump([song.to_dict() for song in self.song_collection.songs], file, indent=4)

    # Sort the song list based on a given sort key and update the UI.
    def sort_songs(self, sort_key):
        # Map the sort key from the UI to the actual song attribute name.
        sort_key_mapping = {'Artist': 'artist', 'Title': 'title', 'Year': 'year', 'Learned': 'is_learned'}
        actual_sort_key = sort_key_mapping.get(sort_key)
        if actual_sort_key:
            self.song_collection.sort(actual_sort_key)
            self.update_song_list()  # Refresh the song list in the UI.

# Run the application.
if __name__ == '__main__':
    SongListApp().run()

