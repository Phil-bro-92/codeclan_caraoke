import unittest
from classes.guest import Guest
from classes.song import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest_1 = Guest("Zoey Robinson", 23, "Mr. Blue Sky", 30)
        self.song_1 = Song("The Racing Rats", "Editors", "An End has a Start", 2007)

    def test_guest_has_name(self):
        self.assertEqual("Zoey Robinson", self.guest_1.name)

    def test_guest_has_age(self):
        self.assertEqual(23, self.guest_1.age)

    def test_guest_has_fav_song(self):
        self.assertEqual("Mr. Blue Sky", self.guest_1.fav_song)

    def test_guest_has_cash(self):
        self.assertEqual(30, self.guest_1.cash)
    
    def test_guest_can_change_fav_song(self):
        self.guest_1.change_fav_song(self.song_1.name)
        self.assertEqual("The Racing Rats", self.guest_1.fav_song)