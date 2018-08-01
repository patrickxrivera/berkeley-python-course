# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, Room):
        self.curr_room = Room
        self.items = []

    def add_item(self, Item):
        self.items.append(Item)

    def remove_item(self, Item):
        self.items.remove(Item)
