from enum import Enum
from typing import List
from copy import deepcopy
import os.path


class Couleur(Enum):
    BLACK = "b"
    WHITE = "w"
    NONE = None


class Queen:
    def __init__(self, pos_x, color, size_bord):
        self.pos_x = pos_x
        self.size_bord = size_bord
        self.set_color(color)

    def __calcul_collum(self):
        res = []
        i = self.pos_x
        while i < self.size_bord * self.size_bord:
            res.append(i)
            i += self.size_bord
        i = self.pos_x - self.size_bord
        while i > -1:

            res.append(i)
            i -= self.size_bord
        res.sort()
        return res

    def __calcul_ligne(self):
        res = []
        i = self.pos_x + 1
        while i % self.size_bord != 0:
            res.append(i)
            i += 1

        i = self.pos_x
        while i % self.size_bord != 0 and i >= 0:
            i -= 1
            res.append(i)

        res.sort()
        return res

    def __calcul_diago(self):
        res = []
        # res.append(self.pos_x)
        diff = self.size_bord + 1
        i = self.pos_x
        while i < self.size_bord * self.size_bord and (i + 1) % self.size_bord != 0:
            i = i + diff
            if i < self.size_bord * self.size_bord:
                res.append(i)

        i = self.pos_x
        while i > -1 and i % self.size_bord != 0:
            i = i - diff
            if i > -1:
                res.append(i)

        diff = self.size_bord - 1
        i = self.pos_x

        while i > -1 and (i + 1) % self.size_bord != 0:
            if i > -1 and i < self.size_bord:
                break
            i = i - diff
            res.append(i)
        i = self.pos_x
        while i < self.size_bord * self.size_bord and i % self.size_bord != 0:
            i = i + diff
            if i < self.size_bord * self.size_bord:
                res.append(i)

        res.sort()
        return res

    def get_hold_cell(self):
        res = self.collum + self.ligne + self.diago
        res.sort()
        return res

    def get_color(self):
        return self.color

    def get_pos_x(self):
        return self.pos_x

    def set_color(self, color: Couleur):
        self.color = color
        if color != Couleur.NONE:
            self.ligne = self.__calcul_ligne()
            self.collum = self.__calcul_collum()
            self.diago = self.__calcul_diago()
        else:
            self.ligne = []
            self.collum = []
            self.diago = []


class White_occup:
    def __init__(self, occup=[]):
        self.occup = occup

    def add_white_occup(self, occup: List[int]):
        self.occup = self.occup + occup

    def check_put_oppose(self, pos_x: int):
        occup = set(self.occup)
        if pos_x in occup:
            return False
        return True

    def remove_occup(self, occup: List[int]):
        for i in occup:
            self.occup.remove(i)


class Black_occup:
    def __init__(self, occup=[]):
        self.occup = occup

    def add_black_occup(self, occup: List[int]):
        self.occup = self.occup + occup

    def check_put_oppose(self, pos_x: int):
        occup = set(self.occup)
        if pos_x in occup:
            return False
        return True

    def remove_occup(self, occup: List[int]):
        for i in occup:
            self.occup.remove(i)


class Chess_bord:
    def __init__(self, size: int):
        # size of the bord
        self.size = size
        # bord empty
        self.bord = [Queen(i, Couleur.NONE, size) for i in range(self.size * self.size)]

    def get_bord(self) -> List[Queen]:
        return self.bord

    # peux-etre useless
    def get_size(self) -> int:
        return self.size

    def put_queen(self, pos_x, color):
        self.bord[pos_x].set_color(color)
        pass

    def get_elemnt(self, pos_x):
        return self.bord[pos_x]

    def check_egal_black_white(self):
        cpt_white = 0
        cpt_black = 0
        for i in self.bord:
            if i.get_color() == Couleur.BLACK:
                cpt_black += 1
            elif i.get_color() == Couleur.WHITE:
                cpt_white += 1

        if cpt_black == cpt_white:
            return True
        return False


def backtracking(
    chess_bord: Chess_bord,
    depth: int = 0,
    white_occup: White_occup = White_occup(),
    black_occup: Black_occup = Black_occup(),
):
    switch: bool = True
    cpt_switch = 0
    if chess_bord.check_egal_black_white():
        print_chess(chess_bord)

    while depth < chess_bord.get_size() * chess_bord.get_size():
        if chess_bord.get_bord()[depth].get_color() == Couleur.NONE:
            if switch:
                if black_occup.check_put_oppose(depth):
                    chess_bord.put_queen(depth, Couleur.WHITE)
                    white_occup.add_white_occup(
                        chess_bord.get_elemnt(depth).get_hold_cell()
                    )
                    backtracking(
                        deepcopy(chess_bord),
                        depth + 1,
                        deepcopy(white_occup),
                        deepcopy(black_occup),
                    )
                    white_occup.remove_occup(
                        chess_bord.get_elemnt(depth).get_hold_cell()
                    )
                    chess_bord.put_queen(depth, Couleur.NONE)
                switch = not switch
                cpt_switch += 1
            else:
                if white_occup.check_put_oppose(depth):
                    chess_bord.put_queen(depth, Couleur.BLACK)
                    black_occup.add_black_occup(
                        chess_bord.get_elemnt(depth).get_hold_cell()
                    )
                    backtracking(
                        deepcopy(chess_bord),
                        depth + 1,
                        deepcopy(white_occup),
                        deepcopy(black_occup),
                    )
                    black_occup.remove_occup(
                        chess_bord.get_elemnt(depth).get_hold_cell()
                    )
                    chess_bord.put_queen(depth, Couleur.NONE)
                switch = not switch
                cpt_switch += 1

        if cpt_switch == 2:
            cpt_switch = 0
            depth += 1


path = os.path.join(
    "./py/peaceably_co-existing_armies_of_queens/resultat/text_json",
    "chess_bord_" + "test" + ".txt",
)
f = open(path, "w")


def print_chess(chess_bord: Chess_bord) -> list:
    chess = chess_bord.get_bord()
    res = []
    for i in chess:
        f.write(str([i.get_color(), i.get_pos_x()]))
        res.append([i.get_color(), i.get_pos_x()])
    f.write("\n")
    print(res)


# quenn = Queen(1, Couleur.BLACK, 3)
# print(quenn.get_hold_cell())


size = 3
chess = Chess_bord(size)
# print_chess(chess)


backtracking(chess)
