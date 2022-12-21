from errors import InvalidDataFormat

from entities.inventary_object import InventaryObject


class Weapon(InventaryObject): 
    def __init__(self, name, attack, durability = 100):
        super(name, durability)

        if type(attack) != 'int' or attack < 0:
            raise InvalidDataFormat('Attack should be positive integer!')

        self.attack = attack

    def print(self):
        return super.print() + f' attack {self.attack}',
