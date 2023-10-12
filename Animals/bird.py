from animal import Animal

class Bird(Animal): 
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        
        self.wingspan = wingspan

    @property
    def get_wingspan(self):
        return self.wingspan

    @get_wingspan.setter
    def get_wingspan(self, new_wingspan):
        self.wingspan = new_wingspan


