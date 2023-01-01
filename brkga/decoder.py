
from .allele import Allele
from .chromosome import Chromosome
from .population import Population

class Decoder(object):

    def decode(self, allele: Allele) -> Allele:
        # map allele to athlete
        allele.decoding = self.decode_allele(allele)
        return allele

    def evaluate(self, chromosome: Chromosome) -> Chromosome:
        # evaluate chromosome fitness
        for allele in chromosome:
            self.decode(allele)
        chromosome.fitness = self.evaluate_chromosome(chromosome)
        return chromosome

    def sort(self, population: Population) -> Population:
        # sort population by fitness
        for chromosome in population:
            if not chromosome.evaluated:
                self.evaluate(chromosome)
        population.chromosomes = self.sort_population(population)
        return population

    def report(self, population: Population) -> Population:
        # override
        return population

    def decode_allele(self, allele: Allele) -> Allele:
        # override
        return allele

    def evaluate_chromosome(self, chromosome: Chromosome) -> dict:
        # override
        return {}

    def sort_population(self, population: Population) -> Population:
        # override
        return population
