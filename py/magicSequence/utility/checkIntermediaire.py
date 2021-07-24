def checkIntermediaire(table, n):
    res = 0
    for i in table:
        res = res + i
    if res > n:
        return False
    else:
        return True
