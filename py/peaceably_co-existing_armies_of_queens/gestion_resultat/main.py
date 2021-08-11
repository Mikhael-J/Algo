from .filtre import filtre
from .converte_solution import converte_solution
import sys
import os

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = os.path.join(
        "./resultat",
        "chess_bord_" + str(n) + "_v6.txt",
    )
    filtre(n, path)
    converte_solution(n, path)
