from animal import *

class Mammal(Animal):
    def __init__ (self, _name, _species):
        super().__init__(_name, _species)


    def give_birth(self):
        return f"{self.get_name} the {self.get_species} has given birth"
