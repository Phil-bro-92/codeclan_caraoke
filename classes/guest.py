class Guest:
    def __init__(self, name, age, fav_song, cash):
        self.name = name
        self.age = age
        self.fav_song = fav_song
        self.cash = cash

    def change_fav_song(self, new_song):
        self.fav_song = new_song