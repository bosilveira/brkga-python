
from .allele import Allele

class Chromosome(object):
    
    chromosome_count: int = 0

    @classmethod
    def count(cls) -> int:
        cls.chromosome_count += 1
        return cls.chromosome_count

    def __init__(self, generation: int = 0, size: int = 12) -> None:
        self.id: int = Chromosome.count()
        self.generation: int = generation
        self.alleles: list[Allele] = [ Allele(locus) for locus in range(1, size + 1) ] 
        self.fitness: dict or None = None
        self.evaluated: bool = False

    def __str__(self) -> str:
        return f"{self.alleles}"

    def __repr__(self) -> str:
        return f"{self.alleles}"

    def reset(self) -> object:
        for allele in self.alleles:
            allele.reset()
        self.fitness = None
        self.evaluated = False
        return self

