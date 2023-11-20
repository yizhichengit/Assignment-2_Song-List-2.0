"""..."""
# TODO: Copy your first assignment to this file, commit, then update to use Song class
# Use SongCollection class if you want to
"""
Name:Yizhi Chen
Date started:21/10/2023
GitHub URL: https://github.com/yizhichengit/starter_a1_songs.git
"""


from song import Song
from songcollection import SongCollection
import json

# 加载歌曲
def load_songs(filename):
    song_collection = SongCollection()
    with open(filename, 'r') as file:
        songs_data = json.load(file)
        for song_data in songs_data:
            song = Song(song_data['title'], song_data['artist'], song_data['year'], song_data['is_learned'])
            song_collection.add_song(song)
    return song_collection

# 显示歌曲列表
def display_songs(song_collection):
    songs = song_collection.songs
    for i, song in enumerate(songs, 1):
        learned_status = 'learned' if song.is_learned else 'not learned'
        print(f"{i}. {song.title} by {song.artist} {song.year} ({learned_status})")

# 添加新歌曲
def add_new_song(song_collection):
    title = input("Title: ")
    artist = input("Artist: ")
    year = int(input("Year: "))  # 这里假设年份输入总是有效的整数
    song_collection.add_song(Song(title, artist, year))

# 更改歌曲的学习状态
def learn_song(song_collection):
    display_songs(song_collection)
    song_number = int(input("Enter the number of the song to mark as learned: "))
    song_to_learn = song_collection.songs[song_number - 1]
    song_to_learn.is_learned = True
    print(f"You have learned {song_to_learn.title}")

# 保存歌曲到文件
def save_songs(song_collection, filename):
    songs_data = []
    for song in song_collection.songs:
        songs_data.append(song.to_dict())  # 假设 Song 类有一个 to_dict 方法
    with open(filename, 'w') as file:
        json.dump(songs_data, file, indent=4)

# 主函数
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

# 显示菜单
def print_menu():
    print("Menu:")
    print("D - Display songs")
    print("A - Add a song")
    print("L - Learn a song")
    print("Q - Quit")

if __name__ == "__main__":
    main()

