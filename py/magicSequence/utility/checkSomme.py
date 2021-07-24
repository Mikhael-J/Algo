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
