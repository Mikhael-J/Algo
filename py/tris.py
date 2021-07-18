

def TrisParInferieur(liste):
    result = []
    while liste != []:
        tmp = liste[0]
        for i in liste:
            if tmp > i:
                tmp = i
        result.append(tmp)
        liste.remove(tmp)
    return result
