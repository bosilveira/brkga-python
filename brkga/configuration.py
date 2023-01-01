
class Configuration(object):

    def __init__(self, n: int = 8, p: int = 1000, pe: int = 100, pm: int = 100, rhoe: float = .8, kmax: int = 500):
        self.n: int = n # chromosome size
        self.p: int = p # population size
        self.pe: int = pe # elite group size
        self.pm: int = pm # mutant group size
        self.rhoe: float = rhoe # inheritance from elite parent
        self.kmax: int = kmax # max number of generations
        self.pc: int = p - pe - pm # crossing-over group size
