import sys
import numpy as np


class patern:
    def __init__(self, size):
        self.size = size
        self.pattern = []
        pass

    def get_pat(self):
        return self.pattern

    def add(self, pat):
        pat = self.__normalizer(pat)
        if self.rotation(pat):
            self.pattern.append(pat)
            return True
        return False

    def check_pattern(self, pat):
        return any((pat == x).all() for x in self.pattern)

    def rotation(self, bord):
        for i in range(4):
            bord = np.rot90(bord)
            if self.check_pattern(bord):
                return False
        return True

    def __normalizer(self, pat):
        pat = np.array_split(pat, self.size)
        pat = np.vstack(pat)
        return pat


if __name__ == "__main__":
    n = int(sys.argv[1])
    a = np.zeros((n ** 2,), dtype=int)
    a[1] = 1
    a[7] = 1
    a[8] = 1
    pat = patern(n)
    pat.add(a)
    print(pat.get_pat())

    b = np.zeros((n ** 2,), dtype=int)
    b[1] = 1
    b[7] = 1
    b[14] = 1
    if pat.add(b):
        print("/////////////////////////////////////")
        print(pat.get_pat())
