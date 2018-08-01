class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print('took an item')

class Treasure(Item):
    def __init__(self, name, description, value):
        self.value = value
        self.used = False
        super().__init__(name, description)

    def on_take(self):
        if self.used:
            return 0
        else:
            self.used = True
            return self.value

class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print("It's not wise to drop your source of light!")
