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
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, ListProperty, ObjectProperty, NumericProperty
from kivy.core.window import Window
from song import Song
from songcollection import SongCollection
import json

class SongListApp(App):
    status_text = StringProperty('')
    song_collection = ObjectProperty(SongCollection())
    learned = NumericProperty(0)
    to_learn = NumericProperty(0)

    def build(self):
        self.song_collection = SongCollection()
        self.song_collection.load_songs('songs.json')

        return Builder.load_file('app.kv')


    def load_songs(self, filename):
        self.song_collection.load_songs(filename)
        self.update_song_list()

    def update_song_list(self):
        # Update song list and status tags
        if self.root and hasattr(self.root.ids, 'songs_box'):
            self.root.ids.songs_box.clear_widgets()
        for song in self.song_collection.songs:
            # Create a button and add it to the interface.
            button_color = (0, 1, 0, 1) if song.is_learned else (1, 0, 0, 1)
            button = Button(text=f'{song.title} by {song.artist} ({song.year})',
                            background_color=button_color,
                            on_release=self.toggle_learned)
            button.song = song
            self.root.ids.songs_box.add_widget(button)
        self.update_status_text()

    def add_song(self):
        title = self.root.ids.title_input.text
        artist = self.root.ids.artist_input.text
        year_text = self.root.ids.year_input.text

        # Error checking.
        if not title or not artist or not year_text:
            self.status_text = "All fields must be completed"
            return

        try:
            year = int(year_text)
            if year <= 0:
                self.status_text = "Year must be > 0"
                return
        except ValueError:
            self.status_text = "Please enter a valid number"
            return

        # add new songs
        self.song_collection.add_song(Song(title, artist, year))
        self.update_song_list()
        self.clear_inputs()

    def clear_inputs(self):
        # Clear input fields
        self.root.ids.title_input.text = ""
        self.root.ids.artist_input.text = ""
        self.root.ids.year_input.text = ""
        self.status_text = ""

    def toggle_learned(self, button_instance):
        song = button_instance.song
        song.is_learned = not song.is_learned
        # Update the text of the status label.
        self.status_text = "You have learned " if song.is_learned else "You need to learn " + song.title
        self.update_song_list()

    def update_status_text(self):
        learned = len([song for song in self.song_collection.songs if song.is_learned])
        to_learn = len(self.song_collection.songs) - learned
        self.learned = self.song_collection.get_number_of_learned_songs()
        self.to_learn = self.song_collection.get_number_of_unlearned_songs()




    def on_stop(self):
        # When the application is about to close, save the song to a JSON file.
        self.save_songs('songs.json')

    def save_songs(self, filename):
        with open(filename, 'w') as file:
            json.dump([song.to_dict() for song in self.song_collection.songs], file, indent=4)

    def sort_songs(self, sort_key):

        sort_key_mapping = {'Artist': 'artist', 'Title': 'title', 'Year': 'year', 'Learned': 'is_learned'}
        actual_sort_key = sort_key_mapping.get(sort_key)
        if actual_sort_key:
            self.song_collection.sort(actual_sort_key)
            self.update_song_list()

if __name__ == '__main__':
    SongListApp().run()


