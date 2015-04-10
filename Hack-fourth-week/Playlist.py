import random
import json


class Playlist:

    def __init__(self, name, repeat=False, shuffle=False):

        self.name = name
        self.repeat = repeat
        self.shuffle = shuffle
        self.playlist = []
        self.current_index = -1

        # Artists
        self.artists = []

        # For next_song
        self.songs_to_be_played = [x for x in range(len(self.playlist))]

    def add_song(self, song):
        self.playlist.append(song)
        self.artists.append(song.artist)

    def remove_song(self, song):
        self.playlist.remove(song)

    def add_songs(self, songs):
        for song in songs:
            self.add_song(song)

    def total_length(self):
        total = 0
        for song in self.playlist:
            total += song.get_length(seconds=True)
        hours = total // 3600
        minutes = (total - hours * 3600) // 60
        seconds = total - hours * 3600 - minutes * 60
        if hours == 0:
            return '00:{}:{}'.format(minutes, seconds)
        return '{}:{}:{}'.format(hours, minutes, seconds)

    def get_artists(self):
        resulting_str = ''
        artists_songs = {}
        for artist in self.artists:
            if artist not in artists_songs:
                artists_songs.update({artist: 0})
            else:
                artists_songs[artist] += 1
        # Making set of unique artirsts
        unique_artists = set(self.artists)
        for artist in unique_artists:
            resulting_str += '{} -> {}'.format(artist,
                                              artists_songs[artist]) + '/n'
            print('{} -> {}'.format(artist, artists_songs[artist]))
        return resulting_str

    def next_song(self):
        # print random.randint()
        if len(self.songs_to_be_played) == 0 and self.repeat:
            self.songs_to_be_played = [x for x in range(len(self.playlist))]
            self.current_index = -1
        if self.shuffle:
            self.current_index = random.choice(self.songs_to_be_played)
            self.songs_to_be_played.remove(self.current_index)
            return self.playlist[self.current_index]
        else:
            self.current_index += 1
            self.songs_to_be_played.remove(self.current_index)
            return self.playlist[self.current_index]

    def pprint_playlist(self):
        resulting_str = ''
        # Evaluating how 'big' columns we'll need
        length_artist_name = len('Artist')
        length_song_name = len('Song')
        length_length = len('Lenght')
        for song in self.playlist:
            if len(song.title) > length_song_name:
                length_song_name = len(song.title)
            if len(song.artist) > length_artist_name:
                length_artist_name = len(song.artist)
            if len(song.get_length()) > length_length:
                length_length = len(song.get_length())
        # Making current row in order to print it
        current_row = '| Artist ' + \
            (length_artist_name - len('Artist')) * ' ' + '|'
        current_row += '| Song ' + (length_song_name - len('Song')) * ' ' + '|'
        current_row += '| Length ' + \
            (length_length - len('Lenght')) * ' ' + '|'
        resulting_str += current_row + '\n'
        print(current_row)
        current_row = '|--' + length_artist_name * '-' + '|'
        current_row += '|--' + length_song_name * '-' + '|'
        current_row += '|--' + length_length * '-' + '|'
        resulting_str += current_row + '\n'
        print(current_row)
        for song in self.playlist:
            current_row = '| ' + song.artist + ' ' + \
                (length_artist_name - len(song.artist)) * ' ' + '|'
            current_row += '| ' + song.title + ' ' + \
                (length_song_name - len(song.title)) * ' ' + '|'
            current_row += '| ' + song.get_length() + ' ' + \
                (length_length - len(song.get_length())) * ' ' + '|'
            resulting_str += current_row + '\n'
            print(current_row)
        return resulting_str

    def prepare_json(self):
        data = {
            "name": self.name,
            "songs": [song.prepare_json() for song in self.playlist]
        }

        return data

    def save(self, indent=True):
        filename = './playlist-data/' + self.name.replace(" ", "-") + ".json"
        with open(filename, "w+") as f:
            f.write(json.dumps(self.prepare_json(), indent=indent))

    @staticmethod
    def load(filename):
        with open('./playlist-data/' + filename, "r") as f:
            contents = f.read()
            data = json.loads(contents)
            p = Playlist(data["name"])

            for dict_song in data["songs"]:
                song = Song(artist=dict_song["artist"], title=dict_song["title"], album=dict_song["album"], length=dict_song["length"])
                p.add_song(song)

            return p

    def change_shuffle_mode(self, shuffle):
        self.shuffle = shuffle

    def change_repeat_mode(self, repeat):
        self.repeat = repeat
