import os.path
import json
from typing import List


def load_data(pathfile: str) -> List[dict]:
    data: List[dict] = []
    file1 = open(pathfile, "r")
    Lines = file1.readlines()
    for line in Lines:
        data.append(json.loads(line.strip()))
    file1.close()
    return data


def filtre(n: int, path: str):
    max_piece = 0
    list_no_double = []
    liste_resultat = load_data(path)

    for i in liste_resultat:
        if max_piece < int([*i][0]):
            max_piece = int([*i][0])

    for i in liste_resultat:
        cpt = 0
        for j in liste_resultat:
            if i == j:
                cpt += 1
        if cpt < 2 and int([*i][0]) == max_piece:
            list_no_double.append(i)

    file1 = open(path, "w")
    for i in list_no_double:
        json.dump(
            i,
            file1,
        )
        file1.write("\n")
    file1.close()
