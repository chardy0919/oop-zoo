from mammal import Mammal
 
class Marsupial(Mammal):
    def __init__ (self, _name, _species):
        super().__init__(_name, _species)


    def carry_baby(self):
        return f"{self.get_name} the {self.get_species} is carrying its baby"
