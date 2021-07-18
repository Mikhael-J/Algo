
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
 
import copy

def backtrack(n, sequence, res, depth=0):
    if depth == len(sequence):
        if checkMagicSequence(sequence):
            res.append(copy.deepcopy(sequence))
        return 0
    for i in range(0, n):
        if sommeInfToLen(sequence):
            if depth < len(sequence):
                sequence[depth] = i
                backtrack(n, copy.deepcopy(sequence), res, depth+1)
            

def sommeInfToLen(table):
    res = 0
    for i in table:
        if not i == None:
            res = res + i
    if res <= len(table):
        return True
    else:
        return False


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


n = 4
res = []
backtrack(n, [None for x in range(n)], res)
print(res)
