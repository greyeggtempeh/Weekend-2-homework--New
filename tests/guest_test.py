import unittest
from src.guest import Guest
from src.song import Song
from src.room import Room

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.guest = Guest("Dandy Wallace", 25.00)
        self.room = Room("Country Bumpkin", 7, 10, 100)
        
    def test_guest_has_name(self):
        self.assertEqual("Dandy Wallace", self.guest.name)
    
    def test_guest_has_a_wallet(self):
        self.assertEqual(25.00, self.guest.wallet)

    def test_guest_can_pay_entry_fee(self):
        room = Room("Country Bumpkin",7, 10.00)
        self.guest.pay_entry(self.room)
        self.assertEqual(15.00, self.guest.wallet)



   
