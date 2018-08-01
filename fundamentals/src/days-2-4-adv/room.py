# Implement a class to hold room information. This should have name and
# description attributes.

get_name = lambda item: item.name

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, Item):
        self.items.append(Item)

    def remove_item(self, Item):
        self.items.remove(Item)
