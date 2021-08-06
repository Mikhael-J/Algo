from typing import List
from copy import deepcopy
from enum import Enum
import os.path
import operator
import time


class Couleur(Enum):
    BLACK = "b"
    WHITE = "w"
    NONE = "n"


class Queen:
    def __init__(self, color: Couleur, pos: int):
        self.color = color
        self.pos = pos

    def get_pos(self) -> int:
        return self.pos

    def get_color(self) -> Couleur:
        return self.color


class Chess_bord:
    def __init__(self, size: int):
        # size of the bord
        self.size = size
        # bord empty
        self.bord = [[] for i in range(self.size)]

        self.nb_white = 0
        self.nb_black = 0

        self.cell_no_access = []

    def put_queen(self, pos_list: int, pos_piece: int, color: Couleur) -> None:

        if color == Couleur.BLACK:
            self.nb_black += 1
        if color == Couleur.WHITE:
            self.nb_white += 1
        # if temporaire # peux-etre useless en function du bactraking
        if self.exist(pos_list, pos_piece):
            self.bord[pos_list].append(Queen(color, pos_piece))

    def remove_queen(self, pos_list: int, color: Couleur):
        last = self.bord[pos_list].pop()
        self.__remove_cell_no_access(pos_list, last.get_pos(), color)
        if last.get_color() == Couleur.BLACK:
            self.nb_black -= 1
        if last.get_color() == Couleur.WHITE:
            self.nb_white -= 1

    def exist(self, pos_list: int, pos_piece: int) -> bool:
        for i in self.bord[pos_list]:
            if i.get_pos() == pos_piece:
                return False
        return True

    def check_egal_black_white(self):
        if self.nb_black == self.nb_white != 0:
            return True
        return False

    def is_safe(self, pos_list: int, pos_piece: int, color: str) -> bool:
        check = True
        res = [[pos_list, pos_piece]]
        # pos actuel not free
        if not self.exist(pos_list, pos_piece):
            return False

        # diagonale
        for i in range(self.size):
            for j in range(self.size):
                if j == pos_piece and i != pos_list:
                    res.append([i, j])

                if i == pos_list and j != pos_piece:
                    res.append([i, j])

                diff_x = abs(i - pos_list)
                diff_y = abs(j - pos_piece)
                if diff_x == diff_y:
                    res.append([i, j])

                try:
                    # queen vertical
                    if i == pos_list:
                        if self.bord[i][j].get_color() != color:
                            check = False

                    # horizontal
                    if (
                        self.bord[i][j].get_pos() == pos_piece
                        and self.bord[i][j].get_color() != color
                    ):
                        check = False
                    diff_x = abs(i - pos_list)
                    diff_y = abs(self.bord[i][j].get_pos() - pos_piece)
                    if diff_x == diff_y and self.bord[i][j].get_color() != color:
                        check = False
                except:
                    ### à gerer
                    pass
        if check:
            self.cell_no_access = self.cell_no_access + res
            # print(self.cell_no_access)

        return check

    def __remove_cell_no_access(self, pos_piece, pos_list, color):
        self.cell_no_access.remove([pos_list, pos_piece])
        for i in range(self.size):
            for j in range(self.size):
                if [i, j] in self.cell_no_access:
                    if j == pos_piece and i != pos_list:
                        self.cell_no_access.remove([i, j])

                    if i == pos_list and j != pos_piece:
                        self.cell_no_access.remove([i, j])

                    diff_x = abs(i - pos_list)
                    diff_y = abs(j - pos_piece)
                    if diff_x == diff_y:
                        self.cell_no_access.remove([i, j])

    def get_bord(self) -> List[List[Queen]]:
        return self.bord

    # peux-etre useless
    def get_size(self) -> int:
        return self.size

    def get_nb_white(self):
        return self.nb_white

    def get_nb_black(self):
        return self.nb_black

    def get_somme_nb_black_white(self):
        return self.nb_black + self.nb_white

    def get_cell_no_access(self):
        # remove dup
        res = list(map(list, set(map(tuple, self.cell_no_access))))
        # cpt = 0
        # for i in range(self.size):
        #     for j in range(self.size):
        #         if [i, j, Couleur.WHITE] in res or [i, j, Couleur.BLACK] in res:
        #             cpt += 1
        return res


def check_break(chess_bord: Chess_bord, pos_liste: int, pos_piece: int):
    # check_more_than_half_same_color_col_or_li
    size = chess_bord.get_size()
    cpt_w_col = 0
    cpt_b_col = 0
    cpt_w_li = 0
    cpt_b_li = 0
    for i in chess_bord.get_bord():
        for j in i:

            if i == chess_bord.get_bord()[pos_liste]:
                if j.get_color() == Couleur.BLACK:
                    cpt_b_col += 1
                if j.get_color() == Couleur.WHITE:
                    cpt_w_col += 1
                if cpt_b_col > (size / 2) + 1:
                    return True
                if cpt_w_col > (size / 2) + 1:
                    return True

            if j.get_pos() == pos_piece:
                if j.get_color() == Couleur.BLACK:
                    cpt_b_li += 1
                if j.get_color() == Couleur.WHITE:
                    cpt_w_li += 1

                if cpt_b_li > (size / 2) + 1:
                    return True
                if cpt_w_li > (size / 2) + 1:
                    return True
    return False


def check_first_piece(chess_bord: Chess_bord):

    if print_chess(chess_bord.get_bord()) != []:
        for i in chess_bord.get_bord():
            for j in i:
                if j.get_color() == Couleur.BLACK:
                    return False
                if j.get_color() == Couleur.WHITE:
                    return True
    return False


def backtracking(chess_bord: Chess_bord, res, switch: bool = True):
    # print(chess_bord.get_cell_no_access())
    if check_first_piece(chess_bord):
        return 0

    j = 0
    i = 0

    if not (
        chess_bord.get_size() * chess_bord.get_size() == chess_bord.get_cell_no_access()
        and chess_bord.check_egal_black_white()
    ) or not (
        chess_bord.get_cell_no_access() - 1
        == chess_bord.get_size() * chess_bord.get_size() - 1
        and chess_bord.check_egal_black_white()
    ):

        while i < chess_bord.get_size():
            if switch:
                color = Couleur.BLACK
            else:
                color = Couleur.WHITE

            if check_break(chess_bord, i, j):
                break

            if chess_bord.is_safe(i, j, color):
                chess_bord.put_queen(i, j, color)
                backtracking(deepcopy(chess_bord), res, deepcopy(not switch))
                chess_bord.remove_queen(i, color)

            j += 1
            if j == chess_bord.get_size():
                i += 1
                j = 0
    if chess_bord.check_egal_black_white():
        if check_dup(chess_bord, res):
            res.append(chess_bord)
            # async
            f.write(
                "{"
                + str(print_chess(chess_bord.get_bord()))
                + str(chess_bord.get_somme_nb_black_white())
                + "},\n"
            )


def check_dup(chess_bord: Chess_bord, res: list) -> bool:
    tmp = print_chess(chess_bord.get_bord())
    tmp2 = []
    for i in res:
        tmp2.append(print_chess(i.get_bord()))
    for i in tmp2:
        if i == tmp:
            return False
    return True


def print_chess(chess_bord) -> list:
    res = []
    for i in range(len(chess_bord)):
        for j in chess_bord[i]:
            res.append([j.get_color().value, i, j.get_pos()])
    return res


if __name__ == "__main__":
    res = []
    n = 5
    path = os.path.join(
        "./py/peaceably_co-existing_armies_of_queens/resultat/text_json",
        "chess_bord_" + str(n) + "_bis.txt",
    )
    f = open(path, "w")
    table = Chess_bord(n)
    backtracking(table, res)
