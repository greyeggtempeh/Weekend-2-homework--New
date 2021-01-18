class Room:

    def __init__(self, name, capacity, entry_cost, till):
        self.name = name
        self.capacity = capacity
        self.entry_cost = entry_cost
        self.playlist = []
        self.guests = []
        self.till = till
    
    def add_guest(self, guest):
        self.guests.append(guest)

    def remove_guest(self, guest):
        self.guests.remove(guest)
    
    def add_song(self, song):
        self.playlist.append(song)
    
    def remove_song(self, song):
        self.playlist.remove(song)

    def keep_track_of_entry(self, guest):
        self.guests.append(guest)
        self.guest.pay_entry(guest)
        self.entry_cost += till
        
