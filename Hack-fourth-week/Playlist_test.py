import unittest
from Song import Song
from Playlist import Playlist
# from io import StringIO
# import sys
# from StringIO import StringIO


class Test_Playlist(unittest.TestCase):

    def setUp(self):
        self.code_songs = Playlist(name="Code", repeat=True, shuffle=True)
        self.song = Song(
            title="Odin", artist="Manowar", album="The Sons of Odin", length="3:44")
        self.code_songs.add_song(self.song)

    def test_init(self):
        self.assertEqual(self.code_songs.name, "Code")
        self.assertEqual(self.code_songs.repeat, True)
        self.assertEqual(self.code_songs.shuffle, True)

    def test_add_song(self):
        self.assertTrue(self.song in self.code_songs.playlist)

    def test_remove_song(self):
        self.code_songs.remove_song(self.song)
        self.assertFalse(self.song in self.code_songs.playlist)

    def test_add_songs(self):
        song1 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:44")
        song3 = Song(
            title="Odin3", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [song1, song2, song3]
        self.code_songs.add_songs(songs)
        self.assertTrue(song1 in self.code_songs.playlist)
        self.assertTrue(song2 in self.code_songs.playlist)
        self.assertTrue(song3 in self.code_songs.playlist)

    def test_total_length(self):
        song1 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [song1, song2]
        self.code_songs.add_songs(songs)

        self.assertEqual(self.code_songs.total_length(), '00:11:12')

    def test_artists(self):

        # Adding songs
        song1 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [song1, song2]
        self.code_songs.add_songs(songs)

        # Testing Print here:
        # out = StringIO()
        # self.code_songs.get_artists()
        # sys.stdout = out
        # output = out.getvalue()

        self.assertTrue(self.code_songs.get_artists(), 'Manowar -> 2')

    def test_next_song(self):
        song1 = Song(
            title="Odin1", artist="Manowar", album="The Sons of Odin", length="3:44")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:44")
        songs = [song1, song2]
        self.code_songs.add_songs(songs)
        self.assertIsInstance(self.code_songs.next_song(), Song)

        # I don't know how to test random :( :D
        # and that's why I make a new playlist
        not_shuffled_playlist = Playlist(
            name="Code1", repeat=True, shuffle=False)
        not_shuffled_playlist.add_songs(songs)
        self.assertEqual(not_shuffled_playlist.next_song(), song1)
        self.assertEqual(not_shuffled_playlist.next_song(), song2)
        self.assertEqual(not_shuffled_playlist.next_song(), song1)

    def test_pprint(self):
        song1 = Song(
            title="Oleeeee", artist="Uhuuuuuuuu", album="The Sons of Odin", length="3:10")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:24")
        songs = [song1, song2]
        self.code_songs.add_songs(songs)
        print()
        self.assertEqual('''| Artist     || Song    || Length |
|------------||---------||--------|
| Manowar    || Odin    || 3:44   |
| Uhuuuuuuuu || Oleeeee || 3:10   |
| Manowar    || Odin2   || 3:24   |
''', self.code_songs.pprint_playlist())

    def test_save(self):
        song1 = Song(
            title="Oleeeee", artist="Uhuuuuuuuu", album="The Sons of Odin", length="3:10")
        song2 = Song(
            title="Odin2", artist="Manowar", album="The Sons of Odin", length="3:24")
        songs = [song1, song2]
        self.code_songs.add_songs(songs)
        self.code_songs.save()
        with open('./playlist-data/Code.json', "r") as f:
            contents = f.read()
            print(contents)

if __name__ == '__main__':
    unittest.main()
