from abc import ABC, abstractclassmethod

class Animal():
    def __init__ (self, _name, _species ):
        self.name = _name
        self.species = _species


    @property 
    def get_name(self):
        return self.name
    
    @get_name.setter
    def set_name(self, new_name):
        self.name = new_name

    @property 
    def get_species(self):
        return self.species
    
    @get_species.setter
    def set_species(self, new_species):
        self.species = new_species

    def speak(self):
        return "Animal sound"