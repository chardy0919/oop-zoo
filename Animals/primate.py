from animal import Animal
 
class Primate(Animal):
    def __init__ (self, _name, _species):
        super().__init__(_name, _species)


    def climb_trees(self):
        return f"{self.get_name} the {self.get_species} is climbing trees"
