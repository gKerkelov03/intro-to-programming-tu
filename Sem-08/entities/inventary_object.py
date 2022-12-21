class InventaryObject: 
    def __init__(self, name, durability = 100):
        self.name = name
        self.durability = durability

    def print(self):
        return f'weapon name: {self.name}, durability: {self.durability}'

