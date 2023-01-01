
from .brkga import *
import random

class Cartola442(Decoder):

    def __init__(self) -> None:
        super().__init__()
        self.gol: list[object] = []
        self.lat: list[object] = []
        self.zag: list[object] = []
        self.mei: list[object] = []
        self.ata: list[object] = []
        self.tec: list[object] = []

    def decode_allele(self, allele: Allele) -> int:
        decoding: int = 0
        if allele.locus in [ 1 ]:
            decoding = random.randint(0, len(self.gol)-1)
        if allele.locus in [ 2, 3 ]:
            decoding = random.randint(0, len(self.lat)-1)
        if allele.locus in [ 4, 5 ]:
            decoding = random.randint(0, len(self.zag)-1)
        if allele.locus in [ 6, 7, 8, 9 ]:
            decoding = random.randint(0, len(self.mei)-1)
        if allele.locus in [ 10, 11 ]:
            decoding = random.randint(0, len(self.ata)-1)
        if allele.locus in [ 12 ]:
            decoding = random.randint(0, len(self.tec)-1)
        return decoding

    def map(self, allele: Allele) -> object:
        reference: object
        if allele.locus in [ 1 ]:
            reference = self.gol[allele.decoding]
        if allele.locus in [ 2, 3 ]:
            reference = self.lat[allele.decoding]
        if allele.locus in [ 4, 5 ]:
            reference = self.zag[allele.decoding]
        if allele.locus in [ 6, 7, 8, 9 ]:
            reference = self.mei[allele.decoding]
        if allele.locus in [ 10, 11 ]:
            reference = self.ata[allele.decoding]
        if allele.locus in [ 12 ]:
            reference = self.tec[allele.decoding]
        return reference

    def evaluate_chromosome(self, chromosome: Chromosome) -> dict:
        home, away, points, price = self.iterate_chromosome(chromosome)
        duplicates = self.count_duplicates(chromosome.alleles[1:3]) + self.count_duplicates(chromosome.alleles[3:5])\
                   + self.count_duplicates(chromosome.alleles[5:9]) + self.count_duplicates(chromosome.alleles[9:11])
        fitness = {
            "duplicates": duplicates,
            "home": home, 
            "away": away, 
            "points": points, 
            "price": price, 
        }
        chromosome.evaluated = True
        return fitness

    def count_duplicates(self, list: list[Allele]) -> int:
        if len(list) < 2:
            return 0
        count: int = 0
        for i in range(len(list)):
            for j in range(i, len(list)):
                if list[i].decoding == list[j].decoding:
                    count += 1 
        return count

    def iterate_chromosome(self, chromosome: Chromosome) -> tuple[int, int, float, float]:
        home: int = 0
        away: int = 0
        points: float = 0.0
        price: float = 0.0
        for allele in chromosome.alleles:
            player = self.map(allele)
            if player.home: home += 1
            if player.away: away += 1
            points += player.points
            price += player.price
        return (home, away, points, price)

