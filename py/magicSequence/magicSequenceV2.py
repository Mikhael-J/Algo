from utility.pile import Pile
from utility.checkMagicSequence import checkMagicSequence


def backTracking(nbElement):
    pos = 0
    pile = Pile()
    [pile.puch(x) for x in range(nbElement)]
    pos += 1
    res = []
    while not(pile.empty()):
        if pos < nbElement:
            for i in range(nbElement):
                pile.puch(i)
            pos += 1
        if len(res) < nbElement:
            res.append(pile.get_remove_Last())
        else:
            if checkMagicSequence(res):
                print(res)
            if res[len(res) - 1] == 0:
                while res[len(res) - 1] == 0:
                    res.pop()
                    pos -= 1
                res.pop()
                res.append(pile.get_remove_Last())
            else:
                res.pop()

backTracking(5)
