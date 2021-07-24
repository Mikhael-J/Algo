from utility.pile import Pile
from utility.checkMagicSequence import checkMagicSequence
from utility.checkIntermediaire import checkIntermediaire
from copy import deepcopy


def backTracking(nbElement: int) -> None:
    pile = Pile()
    pile.puch([])
    while not pile.empty():
        res = pile.get_remove_Last()
        if len(res) >= nbElement:
            if checkMagicSequence(res):
                print(res)
        else:
            for i in range(nbElement):
                res.append(i)
                if checkIntermediaire(res, nbElement):
                    pile.puch(deepcopy(res))
                    res.pop()
                else:
                    res.pop()
                    break


backTracking(10)
