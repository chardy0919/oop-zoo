class ReptileEnclosure():
    def __init__ (self):
        self.reptiles = []

    @property
    def get_reptiles(self):
        return self.reptiles

    @get_reptiles.setter
    def set_reptiles(self, _reptiles):
        self.reptiles = _reptiles

    def add_reptile(self, reptile):
        self.reptiles.append(reptile)
        
