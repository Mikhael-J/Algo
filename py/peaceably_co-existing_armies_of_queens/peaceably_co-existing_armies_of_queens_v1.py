from typing import List
from copy import deepcopy
from enum import Enum
import os.path


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
        # size of the bord
        self.size = size
        # bord empty
        self.bord = [[] for i in range(self.size)]

    def get_elements_vertical(self, pos_list: int) -> List[Queen]:
        return self.bord[pos_list]

    def get_bord(self) -> List[List[Queen]]:
        return self.bord

    # peux-etre useless
    def get_size(self) -> int:
        return self.size

    def put_queen(self, pos_list: int, pos_piece: int, color: str) -> None:
        # if temporaire # peux-etre useless en function du bactraking
        if self.exist(pos_list, pos_piece):
            self.bord[pos_list].append(Queen(color, pos_piece))

    def remove_queen(self, pos_list: int):
        self.bord[pos_list].pop()

    def exist(self, pos_list: int, pos_piece: int) -> bool:
        for i in self.bord[pos_list]:
            if i.get_pos() == pos_piece:
                return False
        return True

    def check_egal_black_white(self):
        cpt_white = 0
        cpt_black = 0
        for i in self.bord:
            for j in i:
                if j.get_color() == Couleur.BLACK:
                    cpt_black += 1
                elif j.get_color() == Couleur.WHITE:
                    cpt_white += 1
        if cpt_black == cpt_white != 0:
            return True
        return False

    def count_piece(self) -> int:
        cpt = 0
        for i in self.bord:
            for j in i:
                cpt += 1
        return cpt


def is_safe(pos_list: int, pos_piece: int, color: str, chess_bord: Chess_bord) -> bool:
    bord = chess_bord.get_bord()
    # pos actuel free
    if not chess_bord.exist(pos_list, pos_piece):
        return False

    # queen vertical
    for queen in chess_bord.get_elements_vertical(pos_list):
        if queen.get_color() != color:
            return False

    # queen horizontal
    for list_queen in bord:
        for queen in list_queen:
            if queen.get_pos() == pos_piece and queen.get_color() != color:
                return False

    # diagonale
    for i in range(len(bord)):
        for j in range(len(bord[i])):
            diff_x = abs(i - pos_list)
            diff_y = abs(bord[i][j].get_pos() - pos_piece)
            if diff_x == diff_y and bord[i][j].get_color() != color:
                return False

    return True


def check_dup(chess_bord: Chess_bord, res: list) -> bool:
    tmp = print_chess(chess_bord.get_bord())
    tmp2 = []
    for i in res:
        tmp2.append(print_chess(i.get_bord()))
    for i in tmp2:
        if i == tmp:
            return False
    return True


def backtracking(chess_bord: Chess_bord, res, k=0, switch: bool = True):
    j = 0
    i = 0
    while i < chess_bord.get_size():
        if switch:
            if is_safe(i, j, Couleur.BLACK, chess_bord):
                chess_bord.put_queen(i, j, Couleur.BLACK)
                backtracking(deepcopy(chess_bord), res, k + 1, not switch)
                chess_bord.remove_queen(i)
        else:
            if is_safe(i, j, Couleur.WHITE, chess_bord):
                chess_bord.put_queen(i, j, Couleur.WHITE)
                backtracking(deepcopy(chess_bord), res, k + 1, not switch)
                chess_bord.remove_queen(i)

        j += 1
        if j == chess_bord.get_size():
            i += 1
            j = 0

    if chess_bord.check_egal_black_white():
        if check_dup(chess_bord, res):
            res.append(chess_bord)


def print_chess(chess_bord) -> list:
    res = []
    for i in range(len(chess_bord)):
        for j in chess_bord[i]:
            res.append([j.get_color(), i, j.get_pos()])
    return res


if __name__ == "__main__":
    res = []
    n = 5
    table = Chess_bord(n)
    backtracking(table, res, 0)
    path = os.path.join(
        "./py/peaceably_co-existing_armies_of_queens/resultat/text_json",
        "chess_bord_" + str(n) + ".txt",
    )
    f = open(path, "w")
    cpt = 0
    color = None
    for i in res:
        table = []
        for j in range(len(i.get_bord())):
            for k in i.get_bord()[j]:
                if Couleur.BLACK == k.get_color():
                    color = "Black"
                elif Couleur.WHITE == k.get_color():
                    color = "White"
                table.append([color, j, k.get_pos()])
        f.write("{" + str(cpt) + ":" + str(table) + "},\n")
        cpt += 1
    f.close()
