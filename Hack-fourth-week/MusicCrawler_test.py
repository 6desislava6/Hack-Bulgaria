import unittest
from MusicCrawler import MusicCrawler


class Test_MusicCrawler(unittest.TestCase):

    def setUp(self):
        path = './Music/'
        self.crawler = MusicCrawler(path)

    def test_generate_playlist(self):
        self.crawler.generate_playlist()
        playlist = self.crawler.generate_playlist()
        self.assertEqual(playlist.pprint_playlist(), '''| Artist                || Song                || Length  |
|-----------------------||---------------------||---------|
| Ed Sheeran            || Don't               || 0:03:39 |
| Red Hot Chili Peppers || Can't Stop          || 0:05:13 |
| Justin Timberlake     || Take Back The Night || 0:05:33 |
''')

if __name__ == '__main__':
    unittest.main()
