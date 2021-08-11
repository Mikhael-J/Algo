import os.path
import json
from typing import List
import gzip
import shutil

n = 3


def converte_solution(n: int, path):

    path2 = os.path.join(
        "./data",
        "n" + str(n) + ".txt.gz",
    )

    chaine = ""
    chaine = list(chaine.zfill(n * n))

    def load_data(pathfile: str) -> List[dict]:
        data: List[dict] = []
        file1 = open(pathfile, "r")
        Lines = file1.readlines()
        for line in Lines:
            data.append(json.loads(line.strip()))
        file1.close()
        return data

    data_file = load_data(path)
    key = [*data_file[0]][0]
    # print(key)
    matrix_lineare = []
    for i in data_file:
        solution = list(i.values())[0]
        for j in solution:
            if j[0] == "b":
                chaine[int(j[1]) * n + int(j[2])] = "2"
            if j[0] == "w":
                chaine[int(j[1]) * n + int(j[2])] = "1"
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
