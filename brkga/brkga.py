
from .decoder import Decoder
from .parameters import Parameters
from .population import Population

class Brkga(object):

    def __init__(self) -> None:
        self.parameters: list = []
        self.decoders: list = []

    def run(self, decoder: Decoder, parameters: Parameters) -> Population:
        population = Population(decoder, parameters)
        while population.generation < parameters.kmax:
            population.evolve()
        population.report()
        return population        