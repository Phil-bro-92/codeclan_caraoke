import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_1 = Room("The Rock Room", 35, 15)
        self.guest_1 = Guest("Zoey Robinson", 23, "Mr. Blue Sky", 30)
        self.guest_2 = Guest("Roy Doran", 45, "Ace of Spades", 100)
        self.song_1 = Song("Mr. Blue Sky", "ELO", "Out of the Blue", 1977)

    def test_room_has_name(self):
        self.assertEqual("The Rock Room", self.room_1.name)

    def test_room_has_capacity(self):
        self.assertEqual(35, self.room_1.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(15, self.room_1.entry_fee)

    def test_check_in_guest_if_not_in_list(self):
        self.room_1.check_in_guest(self.guest_1.name)
        self.assertEqual(["Zoey Robinson"], self.room_1.guest_list)

    def test_check_in_guest_when_guest_in_list(self):
        self.room_1.check_in_guest(self.guest_2.name)
        self.assertEqual(
            "Roy Doran has already checked-in.",
            self.room_1.check_in_guest(self.guest_2.name),
        )

    def test_check_out_guest_if_in_guest_list(self):
        self.room_1.check_in_guest(self.guest_1.name)
        self.room_1.check_out_guest(self.guest_1.name)
        self.assertEqual(0, len(self.room_1.guest_list))
        
    def test_check_out_guest_if_not_in_guest_list(self):
        self.assertEqual("Zoey Robinson is not on list.", self.room_1.check_out_guest(self.guest_1.name))

    def test_add_song_to_song_list_when_song_not_yet_added(self):
        self.room_1.add_song_to_song_list(self.song_1.name)
        self.assertEqual(["Mr. Blue Sky"], self.room_1.song_list)

    def test_add_song_to_song_list_when_already_added(self):
        self.room_1.add_song_to_song_list(self.song_1.name)
        self.assertEqual("Mr. Blue Sky is already listed.", self.room_1.add_song_to_song_list(self.song_1.name))

