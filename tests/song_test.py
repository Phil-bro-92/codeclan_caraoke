import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Mr. Blue Sky", "ELO", "Out of the Blue", 1977)

    def test_song_has_name(self):
        self.assertEqual("Mr. Blue Sky", self.song_1.name)

    def test_song_has_artist(self):
        self.assertEqual("ELO", self.song_1.artist)

    def test_song_has_album(self):
        self.assertEqual("Out of the Blue", self.song_1.album)

    def test_song_has_year(self):
        self.assertEqual(1977, self.song_1.year)