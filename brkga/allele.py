
import random

class Allele(object):

    def __init__(self, locus: int) -> None:
        self.locus: int = locus
        self.key: float = random.random()
        self.decoding: int = 0
        self.reference: None or object = None

    def reset(self) -> object:
        self.key = random.random()
        self.decoding = 0
        return self

