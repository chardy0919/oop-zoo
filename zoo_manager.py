from animal import Animal
from Animals.bird import Bird
from Animals.mammal import Mammal
from Animals.marsupial import Marsupial
from Animals.primate import Primate
from Animals.reptile import Reptile
from reptile_enclosure import ReptileEnclosure
from aviary import Aviary


bird1 = Bird("bird","birdSpecies",3)
mammal1 = Mammal("mammal","mammalSpecies")
marsupial1 = Marsupial("marspial","marspialSpecies")
primate1 = Primate("primate","primateSpecies")
reptile1 = Reptile("reptile","reptileSpecies")

reptile_enclosure = ReptileEnclosure()
reptile_enclosure.add_reptile(reptile1)


print(reptile_enclosure.get_reptiles)