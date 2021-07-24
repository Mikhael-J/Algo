#   @brief [Magic sequence](https://www.csplib.org/Problems/prob019/)
#   implementation

#   @details Solve the magic sequence problem with backtracking

#   "A magic sequence of length $n$ is a sequence of integers $x_0
#   \ldots x_{n-1}$ between $0$ and $n-1$, such that for all $i$
#   in $0$ to $n-1$, the number $i$ occurs exactly $x_i$ times in
#   the sequence. For instance, $6,2,1,0,0,0,1,0,0,0$ is a magic
#   sequence since $0$ occurs $6$ times in it, $1$ occurs twice, etc."
#   Quote taken from the [CSPLib](https://www.csplib.org/Problems/prob019/)
#   website

import sys
import copy
from utility.checkMagicSequence import checkMagicSequence
from utility.checkSomme import sommeInfToLen, sommeTable


def backtrack(n, sequence, res, depth=0):
    if depth == len(sequence):
        if checkMagicSequence(sequence):
            res.append(copy.deepcopy(sequence))
        return 0
    for i in range(0, n):
        if sommeInfToLen(sequence):
            if depth < len(sequence):
                sequence[depth] = i
                backtrack(n, copy.deepcopy(sequence), res, depth + 1)


if __name__ == "__main__":
    try:
        nbElement = int(sys.argv[1])
    except:
        nbElement = None
        pass

    if not nbElement == None:
        res = []
        backtrack(nbElement, [None for x in range(nbElement)], res)
        print(res)
    else:
        print("fist arg need to be a number")
