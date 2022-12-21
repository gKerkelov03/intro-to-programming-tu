from entities.hero import Hero


class Menu:
    def __init__(self):
        self.allHeres = []

    def printCommands():
        print('type 1 for creating a hero!')
        print('type 2 for adding weapon to a hero!')
        print('type 3 for adding secondary object to a hero!')
        print('type 4 for printing all heroes')
        print('type 5 for deleting a hero!')
        pass

    def createHero(name, gender, classInGame):
        hero = Hero(name, gender, classInGame);
        pass

    def addWeaponToHero():
        pass

    def addSecondaryObjectToHero():
        pass

    def printAllHeroes():
        pass

    def deleteHero():
        pass

    def run(self):
        print('the command help will display all the available commands')
        command = input('enter command: ')

        while(command.lower() != 'exit'):
            if(command is '1'):
                self.createHero()
            elif(command is '2'):
                self.addWeaponToHero()
            elif(command is '3'): 
                self.addSecondaryObjectToHero()
            elif(command is '4'):
                self.printAllHeroes()
            elif(command is '5'):
                self.deleteHero()
                
