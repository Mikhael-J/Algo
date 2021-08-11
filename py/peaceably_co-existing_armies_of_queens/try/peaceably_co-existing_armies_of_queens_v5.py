from typing import List
from copy import deepcopy
from enum import Enum
import os.path
import operator
import time
import json
import sys
import math


class Couleur(Enum):
    BLACK = "b"
    WHITE = "w"


class Queen:
    def __init__(self, color: str, pos: int):
        self.color = color
        self.pos = pos

    def get_pos(self) -> int:
        return self.pos

    def get_color(self) -> str:
        return self.color


class Chess_bord:
    def __init__(self, size: int):
        self.size = size
        self.bord = dict((key, []) for key in range(self.size))
        self.cell_accup = []
        self.preview_color = None
        self.nb_white = 0
        self.nb_black = 0
        self.nb_pos_y = dict((key, 0) for key in range(self.size))
        self.nb_pos_x = dict((key, 0) for key in range(self.size))

    def get_bord(self) -> List:
        return self.bord

    def get_size(self) -> int:
        return self.size

    def get_cell_max(self) -> int:
        return self.size * self.size

    def put_queen(self, pos_x: int, pos_y: int, color: Couleur) -> None:
        self.preview_color = color
        self.nb_pos_y[pos_y] = self.nb_pos_y[pos_y] + 1
        self.nb_pos_x[pos_x] = self.nb_pos_x[pos_x] + 1
        if check_color(color):
            self.nb_black += 1
        else:
            self.nb_white += 1

        self.cell_accup.append([pos_x, pos_y])
        self.bord[pos_x].append(Queen(color, pos_y))

    def pop_queen(self, pos_x: int, pos_y: int, color: Couleur) -> None:
        self.nb_pos_y[pos_y] = self.nb_pos_y[pos_y] - 1
        self.nb_pos_x[pos_x] = self.nb_pos_x[pos_x] - 1
        if check_color(color):
            self.nb_black -= 1
        else:
            self.nb_white -= 1
        self.cell_accup.pop()
        self.bord[pos_x].pop()

    def get_somme_nb_black_white(self) -> int:
        return self.nb_black + self.nb_white

    def get_nb_white(self) -> int:
        return self.nb_white

    def get_nb_black(self) -> int:
        return self.nb_black

    def check_same_color_horizontal(self, pos_y) -> bool:
        if self.nb_pos_y[pos_y] == self.size - (
            self.size - math.floor((self.size * 80) / 100)
        ):
            return False
        return True

    def check_same_color_vertical(self, pos_x) -> bool:
        if self.nb_pos_x[pos_x] == self.size - (
            self.size - math.floor((self.size * 80) / 100)
        ):
            return False
        return True

    def check_preview(self):
        return self.preview_color

    # usless for now // check si la moitier de la grille est vide
    def half_empty(self, current_pos_x: int):

        cpt = 0
        if current_pos_x >= math.floor(self.size / 2):
            for key in self.nb_pos_x:
                if self.nb_pos_x[key] == 0:
                    cpt += 1
                else:
                    return True
                if cpt == math.floor(self.size / 2):
                    return False
        return True


def check_color(color: Couleur) -> bool:
    if color == Couleur.BLACK:
        return True
    if color == Couleur.WHITE:
        return False


def check_empty(chess: Chess_bord) -> bool:
    for i in chess:
        for j in chess[i]:
            return True
    return False


def check(chess: Chess_bord, pos_x: int, pos_y: int) -> List[bool]:
    chess_bord = chess.get_bord()
    res = [True, True]
    for x in chess_bord:
        for y in range(len(chess_bord[x])):

            if x == pos_x:
                color = check_color(chess_bord[x][y].get_color())
                if color:
                    res[1] = False
                else:
                    res[0] = False
            # ligne
            if chess_bord[x][y].get_pos() == pos_y:
                color = check_color(chess_bord[x][y].get_color())
                if color:
                    res[1] = False
                else:
                    res[0] = False
            diff_x = abs(x - pos_x)
            diff_y = abs(chess_bord[x][y].get_pos() - pos_y)
            if diff_x == diff_y:
                color = check_color(chess_bord[x][y].get_color())
                if color:
                    res[1] = False
                else:
                    res[0] = False
            if res[0] == False and res[1] == False:
                return res

    return res


def backtrack(chess: Chess_bord, pos_x, pos_y):
    if pos_y == chess.get_size():
        pos_y = 0
        pos_x += 1
    if pos_x == chess.get_size() and chess.get_nb_black() == chess.get_nb_white():
        json.dump(
            {chess.get_somme_nb_black_white(): print_chess(chess.get_bord())},
            f,
        )
        f.write("\n")
    if pos_x < chess.get_size():

        if chess.check_same_color_vertical(pos_x):
            if chess.check_same_color_horizontal(pos_y):
                backtrack(deepcopy(chess), deepcopy(pos_x), deepcopy(pos_y + 1))
                # recu
                possible_color = check(chess, pos_x, pos_y)
                if possible_color[0]:
                    chess.put_queen(pos_x, pos_y, Couleur.BLACK)
                    backtrack(deepcopy(chess), deepcopy(pos_x), deepcopy(pos_y + 1))
                    chess.pop_queen(pos_x, pos_y, Couleur.BLACK)
                    pass
                if check_empty(chess.get_bord()):
                    if possible_color[1]:
                        chess.put_queen(pos_x, pos_y, Couleur.WHITE)
                        backtrack(deepcopy(chess), deepcopy(pos_x), deepcopy(pos_y + 1))
                        chess.pop_queen(pos_x, pos_y, Couleur.WHITE)
                        pass


def print_chess(chess_bord) -> list:
    res = []
    for i in range(len(chess_bord)):
        for j in chess_bord[i]:
            res.append([j.get_color().value, i, j.get_pos()])
    return res


if __name__ == "__main__":
    n = int(sys.argv[1])
    path = "./resultat/text_json/chess_bord_" + str(n) + "_v5.txt"
    f = open(path, "w")
    chess = Chess_bord(n)
    timee = time.time()
    backtrack(chess, 0, 0)
    print(time.time() - timee)
    f.close()

    # # test check
    # chess.put_queen(0, 2, Couleur.WHITE)
    # print("black / white")
    # print(check(chess, 1, 1))
