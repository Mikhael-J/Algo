from typing import List
from copy import deepcopy
from enum import Enum
import os.path
import operator


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

        self.nb_white = 0
        self.nb_black = 0
        self.cell_no_access = []

    def get_elements_vertical(self, pos_list: int) -> List[Queen]:
        return self.bord[pos_list]

    def get_bord(self) -> List[List[Queen]]:
        return self.bord

    # peux-etre useless
    def get_size(self) -> int:
        return self.size

    def put_queen(self, pos_list: int, pos_piece: int, color: Couleur) -> None:

        if color == Couleur.BLACK:
            self.nb_black += 1
        if color == Couleur.WHITE:
            self.nb_white += 1
        # if temporaire # peux-etre useless en function du bactraking
        if self.exist(pos_list, pos_piece):
            self.no_access(pos_list, pos_piece)
            self.bord[pos_list].append(Queen(color, pos_piece))

    def remove_queen(self, pos_list: int):
        last = self.bord[pos_list].pop()
        self.no_access(pos_list, last.get_pos())
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

    def get_nb_white(self):
        return self.nb_white

    def get_nb_black(self):
        return self.nb_black

    def get_somme_nb_black_white(self):
        return self.nb_black + self.nb_white

    def no_access(self, pos_liste: int, pos_piece: int, remove: bool = False):
        if [pos_liste, pos_piece] not in self.cell_no_access:
            check = True
        else:
            check = False

        if not remove:
            self.cell_no_access.append([pos_liste, pos_piece])
        else:
            self.cell_no_access.remove([pos_liste, pos_piece])
        self.__while(
            pos_liste,
            pos_piece,
            -1,
            self.size,
            remove,
            "-",
            "+",
            ">",
            "<",
            "and",
        )
        self.__while(
            pos_liste,
            pos_piece,
            self.size,
            self.size,
            remove,
            "+",
            "+",
            "<",
            "<",
            "and",
        )

        self.__while(
            pos_liste,
            pos_piece,
            -1,
            -1,
            remove,
            "-",
            "-",
            ">",
            ">",
            "and",
        )
        self.__while(
            pos_liste,
            pos_piece,
            self.size,
            -1,
            remove,
            "+",
            "-",
            "<",
            ">",
            "and",
        )
        self.__while(
            pos_liste,
            0,
            pos_liste,
            self.size,
            remove,
            "*",
            "+",
            "==",
            "<",
            "and",
        )
        self.__while(
            0,
            pos_piece,
            self.size,
            pos_piece,
            remove,
            "+",
            "*",
            "<",
            "==",
            "and",
        )
        return check

    def __while(
        self,
        x: int,
        y: int,
        compXto: int,
        compYto: int,
        remove: bool,
        operatorOpX: str,
        operatorOpY: str,
        operatorBoucleX,
        operatorBoucleY,
        operatorLog: str = "None",
    ):
        ops = {
            ">": operator.gt,
            "<": operator.lt,
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "==": operator.eq,
            "and": operator.and_,
        }

        if operatorOpY != "None":
            y = ops[operatorOpY](y, 1)
        if operatorOpX != "None":
            x = ops[operatorOpX](x, 1)

        while ops[operatorLog](
            ops[operatorBoucleX](x, compXto), ops[operatorBoucleY](y, compYto)
        ):

            if not remove:
                self.cell_no_access.append([x, y])
            else:
                self.cell_no_access.remove([x, y])
            if operatorOpY != "None":
                y = ops[operatorOpY](y, 1)
            if operatorOpX != "None":
                x = ops[operatorOpX](x, 1)

    def get_cell_nb_no_access(self):
        # remove dup from list of list
        return len(list(map(list, set(map(tuple, self.cell_no_access)))))


########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
########################################################
def is_safe(pos_list: int, pos_piece: int, color: str, chess_bord: Chess_bord) -> bool:
    bord = chess_bord.get_bord()
    # pos actuel not free
    if not chess_bord.exist(pos_list, pos_piece):
        return False

    # queen vertical
    for queen in chess_bord.get_elements_vertical(pos_list):
        if queen.get_color() != color:
            return False

    # diagonale
    for i in range(len(bord)):
        for j in range(len(bord[i])):
            # horizontal
            if bord[i][j].get_pos() == pos_piece and bord[i][j].get_color() != color:
                return False
            diff_x = abs(i - pos_list)
            diff_y = abs(bord[i][j].get_pos() - pos_piece)
            if diff_x == diff_y and bord[i][j].get_color() != color:
                return False

    return True


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
    print(chess_bord.get_cell_nb_no_access())
    if check_first_piece(chess_bord):
        return 0

    j = 0
    i = 0
    while i < chess_bord.get_size():
        if switch:
            color = Couleur.BLACK
        else:
            color = Couleur.WHITE

        if check_break(chess_bord, i, j):
            break

        if is_safe(i, j, color, chess_bord):
            chess_bord.put_queen(i, j, color)
            backtracking(deepcopy(chess_bord), res, deepcopy(not switch))
            chess_bord.remove_queen(i)

        j += 1
        if j == chess_bord.get_size():
            i += 1
            j = 0
    if chess_bord.check_egal_black_white():
        f.write(
            "{"
            + str(print_chess(chess_bord.get_bord()))
            + str(chess_bord.get_somme_nb_black_white())
            + "},\n"
        )


def print_chess(chess_bord) -> list:
    res = []
    for i in range(len(chess_bord)):
        for j in chess_bord[i]:
            res.append([j.get_color(), i, j.get_pos()])
    return res


if __name__ == "__main__":
    res = []
    n = 3
    path = os.path.join(
        "./py/peaceably_co-existing_armies_of_queens/resultat/text_json",
        "chess_bord_" + str(n) + "_bis_bis.txt",
    )
    f = open(path, "w")
    table = Chess_bord(n)
    backtracking(table, res)
