from errors import CharacterExists, InvalidDataFormat


class Hero: 
    allNames = []

    def __init__(self, name, gender, classInGame, mainWeapon = None, secondaryObject = None):

        if name in Hero.allNames:
            raise CharacterExists

        if(gender != 'm' or gender != 'f' or gender != 'female' or gender != 'male'):
            raise InvalidDataFormat('Gender should be either female (f) or male (m)')

        if classInGame != 'warrior' or classInGame != 'priest' or classInGame != 'rogue'or classInGame != 'mage':
            raise InvalidDataFormat('Class in game should be Warrior, Mage, Priest or Rogue')

        self.name = name
        self.gender = gender
        self.classInGame = classInGame
        self.mainWeapon = mainWeapon
        self.secondaryObject = secondaryObject

        Hero.allNames.append(name)

    def print(self):
        mainWeaponText = 'None' if self.mainWeapon is None else self.mainWeapon.print()

        secondaryObjectText = 'None' if self.secondaryObject is None else self.secondaryObject.print()

        return f'Hero name: {self.name}, gender: {self.gender}, classInGame: {self.classInGame}, mainWeapon: {mainWeaponText}, secondaryObject: {secondaryObjectText}' 
