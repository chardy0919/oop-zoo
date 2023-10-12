from animal import Animal

class Bird(Animal): 
    def __init(self, name, species, wingspan):
        super().__init__(name, species)
        
        self._wingspan = wingspan

    @property
    def get_wingspan(self):
        return self._wingspan

    @get_wingspan.setter
    def get_wingspan(self, new_wingspan):
        self._wingspan = new_wingspan


