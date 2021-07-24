def checkMagicSequence(table):
    for i in range(len(table)):
        count = 0
        for j in range(len(table)):
            if i == table[j]:
                count += 1
        if not count == table[i]:
            return False
    if sommeTable(table) == len(table):
        return True
    return False


def sommeTable(table):
    res = 0
    for i in table:
        if not i == None:
            res = res + i
    return res
