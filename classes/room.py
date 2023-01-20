class Room:
    def __init__(self, name, capacity, entry_fee):
        self.name = name
        self.capacity = capacity
        self.entry_fee = entry_fee
        self.song_list = []
        self.guest_list = []

    def check_in_guest(self, guest_name):
        if guest_name not in self.guest_list:
            self.guest_list.append(guest_name)
        else:
            return f"{guest_name} has already checked-in."

    def check_out_guest(self, guest_name):
        if guest_name in self.guest_list:
            self.guest_list.remove(guest_name)
        else:
            return f"{guest_name} is not on list."
    
    def add_song_to_song_list(self, song_name):
        if song_name not in self.song_list:
            self.song_list.append(song_name)
        else:
            return f"{song_name} is already listed."
