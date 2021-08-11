import os.path
import json
from typing import List
import gzip
import shutil


def converte_solution(n: int, path):
    path2 = os.path.join(
        "./data",
        "n" + str(n) + ".txt.gz",
    )
    liste_resultat = load_data(path)
    key = [*liste_resultat[0]][0]
    matrix_lineare = []
    chaine = ""
    chaine = list(chaine.zfill(n * n))
    for l in liste_resultat:
        cpt = 0
        for i in range(n):
            for j in range(n):
                if l[key][cpt] == 2:
                    chaine[i * n + j] = str(l[key][cpt])
                if l[key][cpt] == 1:
                    chaine[i * n + j] = str(l[key][cpt])
                cpt += 1
        matrix_lineare.append({"f": key, "s": "".join(chaine)})
        chaine = ""
        chaine = list(chaine.zfill(n * n))
    file1 = open(path, "w")
    for i in matrix_lineare:
        json.dump(
            i,
            file1,
        )
        file1.write("\n")
    file1.close()

    with open(path, "rb") as f_in:
        with gzip.open(path2, "wb") as f_out:
            shutil.copyfileobj(f_in, f_out)


def load_data(pathfile: str) -> List[dict]:
    data: List[dict] = []
    file1 = open(pathfile, "r")
    Lines = file1.readlines()
    for line in Lines:
        data.append(json.loads(line.strip()))
    file1.close()
    return data
