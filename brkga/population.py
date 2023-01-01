
from .decoder import Decoder
from .configuration import Configuration
from .chromosome import Chromosome
import random

class Population(object):

    def __init__(self, decoder: Decoder, parameters: Configuration) -> None:
        self.decoder: Decoder = decoder
        self.parameters: Configuration = parameters
        self.chromosomes: Chromosome = [ Chromosome(generation = 0) for index in range(self.parameters.p) ]
        self.generation: int = 0

    def reset(self) -> object:
        for chromosome in self.chromosomes:
            chromosome.reset()
        self.generation = 0
        return self

    def sort(self) -> object:
        self.decoder.sort(self)
        return self

    def report(self) -> object:
        self.decoder.report(self)
        return self

    def evolve(self) -> object:
        self.generation += 1
        elite = self.get_elite()
        nelite = self.get_nelite()
        mutant = self.get_mutant()
        crossover = self.get_crossover(elite, nelite)
        next = elite + mutant + crossover
        self.chromosomes = next
        return self

    def get_elite(self) -> list:
        return self.chromosomes[0:self.parameters.pe]

    def get_nelite(self) -> list:
        return self.chromosomes[self.parameters.pe:]

    def get_mutant(self) -> list:
        return [ Chromosome(self.generation) for _ in range(self.parameters.pm) ]

    def get_crossover(self, elite, nelite) -> list:
        crossover = []
        for index in range(self.parameters.pc):
            crossover.append(index)
        return crossover

    def crossover(self, chromosome_a, chromosome_b) -> Chromosome:
        alleles = []
        for index in range(self.parameters.n):
            allele = chromosome_a.alleles[index] if random.random() <= self.parameters.rhoe else chromosome_b.alleles[index]
            alleles.append(allele)
        new_chromosome = Chromosome(generation = self.generation, size = self.parameters.n)
        new_chromosome.alleles = alleles
        return new_chromosome
