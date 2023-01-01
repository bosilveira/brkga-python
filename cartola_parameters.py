
from .brkga import Parameters

class TCC(Parameters):

    def __init__(self, n = 8, p = 1000, pe = 100, pm = 100, rhoe = .8, kmax = 500):
        self.n = n # chromosome size
        self.p = p # population size
        self.pe = pe # elite group size
        self.pm = pm # mutant group size
        self.rhoe = rhoe # inheritance from elite parent
        self.kmax = kmax # max number of generations
        self.pc = p - pe - pm # crossing-over group size