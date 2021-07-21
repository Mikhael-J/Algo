from py.utility.pile import Pile

def backTracking(nbElement):
    pos = 0
    pile = Pile()
    check = True
    res = []
    while check:
        if pos < nbElement:
            for i in range(nbElement):
                pile.add(i)

            pos += 1
        if pile.getPile() == []:
            check = False
        else:
            if len(res) < nbElement:
                res.append(pile.get_remove_Last())
            else:
                if checkMagicSequence(res):
                    print(res)
                if res[len(res)-1] == 0:
                    while res[len(res)-1] == 0:
                        res.pop()
                        pos -= 1
                    res.pop()
                    res.append(pile.get_remove_Last())
                else:
                    res.pop()
                pass

    pass


def sommeTable(table):
    res = 0
    for i in table:
        if not i == None:
            res = res + i
    return res


def checkMagicSequence(table):
    for i in range(len(table)):
        count = 0
        for j in range(len(table)):
            if(i == table[j]):
                count += 1
        if(not count == table[i]):
            return False
    if(sommeTable(table) == len(table)):
        return True
    return False


backTracking(4)
