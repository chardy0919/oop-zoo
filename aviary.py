class Aviary():
    def __init__ (self):
        self.birds = []

    @property
    def get_birds(self):
        return self.birds

    @get_birds.setter
    def set_bird(self, _birds):
        self.birds = _birds

    def add_bird(self, bird):
        self.birds.append(bird)
        
