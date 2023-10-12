from animal import Animal

class Reptile(Animal):

    def __init__(self, _name, _species):
        super().__init__( _name, _species)

    def bask_in_sun(self):
        return f"{self.name} the {self.species} is basking in the sun"