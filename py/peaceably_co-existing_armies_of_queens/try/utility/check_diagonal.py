def is_safe(chess_bord, pos_x, pos_y, color):
    if color == "black":
        color = "white"
    else:
        color == "black"

    size_bord = len(chess_bord)
    # [bas x, bas y, haut x, haut y]
    diagonale = [0, 0, 0, 0]
    if chess_bord[pos_x][pos_y]:
        return False
    for x in range(size_bord):
        if chess_bord[x][pos_y] == color:
            return False
    for y in range(size_bord):
        if chess_bord[pos_x][y] == color:
            return False
    for x_y in range(size_bord):
        # [diagonale_cote_gauche_bas_x, diagonale_cote_gauche_bas_y, diagonale_cote_gauche_haut_x, diagonale_cote_gauche_haut_y]
        diagonale = [
            abs(x_y - pos_x),
            abs(x_y - pos_y),
            abs(x_y - pos_x),
            abs(x_y + pos_y),
        ]
        if not (
            diagonale[0] >= size_bord
            or diagonale[1] >= size_bord
            or diagonale[2] >= size_bord
            or diagonale[3] >= size_bord
        ):
            if (
                chess_bord[diagonale[0]][diagonale[1]] == color
                or chess_bord[diagonale[2]][diagonale[3]] == color
            ):
                return False
            if (
                diagonale[0] == 0
                or diagonale[1] == 0
                or diagonale[2] == 0
                or diagonale[3] == 0
            ):
                break

    for x_y in range(size_bord):
        # [diagonale_cote_droit_bas_x, diagonale_cote_droit_bas_y, diagonale_cote_droit_haut_x, diagonale_cote_droit_haut_y]
        diagonale = [
            abs(x_y + pos_x),
            abs(x_y - pos_y),
            abs(x_y + pos_x),
            abs(x_y + pos_y),
        ]
        if not (
            diagonale[0] >= size_bord
            or diagonale[1] >= size_bord
            or diagonale[2] >= size_bord
            or diagonale[3] >= size_bord
        ):

            if (
                chess_bord[diagonale[2]][diagonale[3]] == color
                or chess_bord[diagonale[0]][diagonale[1]] == color
            ):
                return False
            if (
                diagonale[0] == 0
                or diagonale[1] == 0
                or diagonale[2] == 0
                or diagonale[3] == 0
            ):
                break

    return True


tab = [
    [None, None, None, None, None],
    [None, None, None, None, None],
    ["white", None, None, None, None],
    [None, "black", None, None, None],
    [None, None, None, None, None],
]


print(is_safe(tab, 1, 0, "black"))
