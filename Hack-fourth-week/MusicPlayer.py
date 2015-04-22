from subprocess import Popen, PIPE
# import time
from Playlist import Playlist
from MusicCrawler import MusicCrawler


class MusicPlayer:

    def __init__(self):
        self.process = Popen(["mpg123", ''], stdout=PIPE, stderr=PIPE)
        self.main_playlist = Playlist(name="Code", repeat=True, shuffle=True)

    def __play(self, mp3Path):
        process = Popen(["mpg123", mp3Path], stdout=PIPE, stderr=PIPE)
        return process

    def __stop(self):
        self.process.kill()

    def add_songs_from_dir(self, another_dir):
        crawler = MusicCrawler(another_dir)
        another_playlist = crawler.generate_playlist()
        for song in another_playlist.playlist:
            self.main_playlist.add_song(song)
        self.main_playlist.songs_to_be_played = [
            x for x in range(len(self.main_playlist.playlist))]

    def change_shuffle_mode(self, shuffle):
        self.main_playlist.change_shuffle_mode(shuffle)

    def change_repeat_mode(self, repeat):
        self.main_playlist.change_repeat_mode(repeat)

    def play_next_song(self):
        current_song = self.main_playlist.next_song()
        self.process = self.__play(current_song.path)
        print('Now playing: ' + str(current_song))

    def stop_playing_all(self):
        self.__stop()

    def show_playlist(self):
        self.main_playlist.pprint_playlist()

# p = play("Music/Ed Sheeran - Dont.mp3")
# time.sleep(30)
# stop(p)
