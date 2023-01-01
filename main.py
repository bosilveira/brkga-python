
from .brkga import Brkga, Population
from .cartola_decoders import Cartola442
from .cartola_parameters import TCC

brkga = Brkga()
population = Population(Cartola442, TCC)

brkga.run()