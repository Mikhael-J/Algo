def count_cell_occup(bord, pos, color, remove):
    chess_bord = bord.get_bord()
    number_cell = bord.get_size() * bord.get_size()
    ligne_start = pos % bord.get_size()
    vertical_start = pos - pos % bord.get_size()
    cpt = 0

    while cpt < bord.get_size():
        if chess_bord[ligne_start] == color:
            return False
        if chess_bord[vertical_start] == color:
            return False
        cpt += 1
        vertical_start += 1
        ligne_start += bord.get_size()

    start_one_diago_up_gauche = pos
    start_one_diago_down_droite = pos
    diff = bord.get_size() - 1

    while (
        start_one_diago_up_gauche > 0
        and (start_one_diago_up_gauche + 1) % bord.get_size() != 0
    ):
        start_one_diago_up_gauche -= diff
        if start_one_diago_up_gauche > 0:
            if chess_bord[start_one_diago_up_gauche] == color:
                return False

    while (
        start_one_diago_down_droite < number_cell - bord.get_size()
        and start_one_diago_down_droite % bord.get_size() != 0
    ):
        start_one_diago_down_droite += diff
        if chess_bord[start_one_diago_down_droite] == color:
            return False

    start_one_diago_up_droite = pos
    start_one_diago_down_gauche = pos
    diff = bord.get_size() + 1

    while (
        start_one_diago_up_droite + 1
    ) % bord.get_size() != 0 and start_one_diago_up_droite < number_cell - bord.get_size():
        start_one_diago_up_droite += diff
        if chess_bord[start_one_diago_up_droite] == color:
            return False

    while (
        start_one_diago_down_gauche > 0
        and start_one_diago_down_gauche % bord.get_size() != 0
    ):
        start_one_diago_down_gauche -= diff

        if start_one_diago_down_gauche >= 0:
            if chess_bord[start_one_diago_down_gauche] == color:
                return False
    return True
