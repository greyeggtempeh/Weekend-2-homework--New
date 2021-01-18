import unittest
from src.room import Room
from src.guest import Guest
from src.song import Song


class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Country Bumpkin", 7, 10, 100)
        self.guest = Guest("Dandy Wallace", 25.00)
        self.song = Song("Just dropped in", "Kenny Rogers")

    def test_room_has_name(self):
        self.assertEqual("Country Bumpkin", self.room.name)

    def test_room_has_capacity(self):
        self.assertEqual(7, self.room.capacity)

    def test_room_has_entry_fee(self):
        self.assertEqual(10, self.room.entry_cost)

    def test_room_has_till(self):
        self.assertEqual(100, self.room.till)
    
    def test_room_has_guests(self):
        self.assertEqual(0, len(self.room.guests))

    def test_room_starts_empty(self):
        self.assertEqual(0, len(self.room.guests))

    def test_playlist_can_add_song(self):
        self.room.add_song(self.song)
        self.room.remove_song(self.song)
        self.assertEqual(0, len(self.room.playlist))
    
    def test_room_can_allow_guests_in_and_out(self): 
        self.room.add_guest(self.guest) 
        self.room.remove_guest(self.guest)
        self.assertEqual(0, len(self.room.guests))

    # def test_calculate_total_entry_fees(self):
    #     self.room.entry_cost(self.room)
    #     self.guest.pay_entry(self.guest)
    #     self.guests.append(guest)
    #     self.assertEqual(10, self.room.guests)

    def test_calculate_total_entry_fees(self):
        self.room.add_guest(self.guest) 
        self.guest.pay_entry(self.guest)
        self.assertEqual(1, len(self.room.guests))
        self.assertEqual(10, self.room.till)


    