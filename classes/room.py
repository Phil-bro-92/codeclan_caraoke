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

    def room_has_enough_space(self):
        if len(self.guest_list) < self.capacity:
            return f"{self.name} has enough space."
        else:
            return f"Sorry, {self.name} is at capacity."

    def check_customer_can_afford_entry(self, customer_cash):
        if customer_cash >= self.entry_fee:
            return "Customer can afford entry."
        else:
            return "Customer can not afford entry."
