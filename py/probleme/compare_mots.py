# mot1,mot2 size egal
# mot1,mot2 str or int
def compare(mot1: str or int, mot2: str or int):
    # si number
    if type(mot1) == int:
        mot1 = [int(i) for i in str(mot1)]
        mot2 = [int(i) for i in str(mot2)]

    for i in range(len(mot1)):
        if mot1[i] == mot2[i]:
            continue

        if mot1[i] < mot2[i]:
            return "mot2 est le plus grand"

        if mot1[i] > mot2[i]:
            return "mot1 est le plus grand"

    return "mot1 = mot2"


print(compare(12, 22))
