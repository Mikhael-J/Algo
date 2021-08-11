from typing import List
from copy import deepcopy
from enum import Enum
import os.path
import operator
import time
import json
import sys
import math
import numpy

WHITE = 1
BLACK = 2


class Chess_bord:
    def __init__(self, size: int):
        self.size = size
        self.bord = [0 for i in range(self.size * self.size)]
        self.nb_white = 0
        self.nb_black = 0
        self.cell_occup = {key: 0 for key in range(self.size * self.size)}

    def get_size(self):
        return self.size

    def get_bord(self):
        return self.bord

    def put_queen(self, pos, color: int):

        if color == WHITE:
            self.nb_white += 1
        if color == BLACK:
            self.nb_black += 1

        self.bord[pos] = color

    def remove_queen(self, pos):
        if self.bord[pos] == WHITE:
            self.nb_white -= 1

        if self.bord[pos] == BLACK:
            self.nb_black -= 1

        self.bord[pos] = 0

    def get_nb_white(self) -> int:
        return self.nb_white

    def get_nb_black(self) -> int:
        return self.nb_black

    def get_somme_nb_black_white(self) -> int:
        return self.nb_black + self.nb_white

    def check(self, pos, color):
        chess_bord = self.bord
        number_cell = self.size ** 2
        ligne_start = pos % self.size
        vertical_start = pos - pos % self.size
        cpt = 0
        res = True
        # get_cell_occup = self.cell_occup

        while cpt < self.size:
            # if get_cell_occup[ligne_start] == 0:
            #     get_cell_occup[ligne_start] += 1
            # if get_cell_occup[vertical_start] == 0:
            #     get_cell_occup[vertical_start] += 1

            if chess_bord[ligne_start] == color:
                res = False
            if chess_bord[vertical_start] == color:
                res = False
            cpt += 1
            vertical_start += 1
            ligne_start += self.size

        start_one_diago_up_gauche = pos
        start_one_diago_down_droite = pos
        diff = self.size - 1

        while (
            start_one_diago_up_gauche > 0
            and (start_one_diago_up_gauche + 1) % self.size != 0
        ):
            start_one_diago_up_gauche -= diff

            if start_one_diago_up_gauche > 0:
                # if get_cell_occup[start_one_diago_up_gauche] == 0:
                #     get_cell_occup[start_one_diago_up_gauche] += 1

                if chess_bord[start_one_diago_up_gauche] == color:
                    res = False

        while (
            start_one_diago_down_droite < number_cell - self.size
            and start_one_diago_down_droite % self.size != 0
        ):
            start_one_diago_down_droite += diff
            # if get_cell_occup[start_one_diago_down_droite] == 0:
            #     get_cell_occup[start_one_diago_down_droite] += 1

            if chess_bord[start_one_diago_down_droite] == color:
                res = False

        start_one_diago_up_droite = pos
        start_one_diago_down_gauche = pos
        diff = self.size + 1

        while (
            start_one_diago_up_droite + 1
        ) % self.size != 0 and start_one_diago_up_droite < number_cell - self.size:
            start_one_diago_up_droite += diff
            # if get_cell_occup[start_one_diago_up_droite] == 0:
            #     get_cell_occup[start_one_diago_up_droite] += 1

            if chess_bord[start_one_diago_up_droite] == color:
                res = False

        while (
            start_one_diago_down_gauche > 0
            and start_one_diago_down_gauche % self.size != 0
        ):
            start_one_diago_down_gauche -= diff
            # if get_cell_occup[start_one_diago_up_droite] == 0:
            #     get_cell_occup[start_one_diago_up_droite] += 1

            if start_one_diago_down_gauche >= 0:
                if chess_bord[start_one_diago_down_gauche] == color:
                    res = False

        # if res:
        #     self.cell_occup = get_cell_occup
        return res


# force la premiere cell a etre changer d'entre blanche
def check_empty(chess: Chess_bord) -> bool:
    for i in chess:
        if i != 0:
            return True
    return False


# gagne ~0.5s
def first_empty_col(chess: Chess_bord, pos):
    check = True
    if pos >= chess.get_size() / 2:
        check = False
    for i in range(math.floor(chess.get_size() / 2)):
        if chess.get_bord()[i] != 0:
            check = True
    return check


def backtrack(chess: Chess_bord, pos=0):

    if (
        pos == chess.get_size() ** 2
        and chess.get_nb_black() == chess.get_nb_white() != 0
    ):
        json.dump(
            {chess.get_somme_nb_black_white(): chess.get_bord()},
            f,
        )
        f.write("\n")

    if pos < chess.get_size() * chess.get_size():
        if first_empty_col(chess, pos):
            backtrack(deepcopy(chess), deepcopy(pos + 1))

        if chess.check(pos, WHITE):
            chess.put_queen(pos, BLACK)
            backtrack(deepcopy(chess), deepcopy(pos + 1))
            chess.remove_queen(pos)

        if check_empty(chess.get_bord()):
            if chess.check(pos, BLACK):
                chess.put_queen(pos, WHITE)
                backtrack(deepcopy(chess), deepcopy(pos + 1))


if __name__ == "__main__":
    n = int(sys.argv[1])
    path = "./resultat/chess_bord_" + str(n) + "_v6.txt"
    f = open(path, "w")
    chess = Chess_bord(n)
    timee = time.time()
    backtrack(chess, 0)

    print("time: " + str(time.time() - timee))
    f.close()
