import unittest
from src.song import Song
from src.room import Room
from src.guest import Guest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("When you're hot you're hot", "Jerry Reed")
        self.song2 = Song("Just dropped in", "The First Edition")
        
    def test_song_has_name(self):
        self.assertEqual("When you're hot you're hot", self.song.title)
    
    
    