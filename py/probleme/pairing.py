dictio = {"{": "}", "'": "'", '"': '"', "<": ">", "[": "]"}


def checkpairing(charas: str):
    pile = []
    for i in charas:
        if i in dictio:
            pile.append(i)
        if i in dictio[pile[-1]]:
            pile.pop()
    if pile == []:
        return True
    return False


if __name__ == "__main__":
    print(checkpairing("[{[}]]"))
