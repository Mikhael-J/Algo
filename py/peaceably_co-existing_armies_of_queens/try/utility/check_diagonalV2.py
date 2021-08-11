def is_safe(chess_bord, pos_list, pos_piece):
    size_bord = len(chess_bord)
    # [vertical_droite_haut, vertical_droite_bas, vertical_gauche_haut, vertical_gauche_bas]
    diagonale = [pos_piece, pos_piece, pos_piece, pos_piece]
    for i in range(size_bord):
        # check horizontal
        if i == pos_list:
            if chess_bord[i] != []:
                return False
        # check vertical
        for j in chess_bord[i]:
            if j == pos_piece:
                return False
    for i in range(pos_list, size_bord, 1):
        for j in chess_bord[i]:
            if j == diagonale[1] or j == diagonale[0]:
                return False
        diagonale[0] = diagonale[0] + 1
        diagonale[1] = diagonale[1] - 1

    for i in range(pos_list, -1, -1):
        for j in chess_bord[i]:
            if j == diagonale[2] or j == diagonale[3]:
                return False
        diagonale[2] = diagonale[2] + 1
        diagonale[3] = diagonale[3] - 1

    return True


tableTest = [[], [], [2], [], []]

print(is_safe(tableTest, 1, 0))
