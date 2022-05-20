from typing import List


class alphabet:
    # ordre_regression []
    # alphabet []
    def __init__(self, ordre_regression: List, alphabet=[]):
        self._alphabet = alphabet
        self._ordre_regression = ordre_regression
        pass

    def compare(self, mot1, mot2):
        mot1, mot2 = self._type(mot1, mot2)

        if len(mot1) != len(mot2):
            return False

        self._ifEmptyAlphabet(mot1, mot2)

        for i in range(len(mot1)):

            if mot1[i] in self._ordre_regression or mot2[i] in self._ordre_regression:
                return "no relation d'ordre"

            if mot1[i] in self._alphabet and mot2[i] in self._alphabet:
                indexMot1 = self._ordre_regression.index(mot1[i])
                indexMot2 = self._ordre_regression.index(mot2[i])

                if indexMot1 == indexMot2:
                    continue
                if indexMot1 > indexMot2:
                    return "mot1 > mot2"
                if indexMot2 > indexMot1:
                    return "mot2 > mot1"

            else:
                return "mot inconue"
        return "mot1 = mot2"

    def _type(self, mot1, mot2):
        if type(mot1) == int:
            mot1 = [int(i) for i in str(mot1)]
            mot2 = [int(i) for i in str(mot2)]
        return mot1, mot2

    def _ifEmptyAlphabet(self, mot1, mot2):
        if self._alphabet == []:
            for i in range(len(mot1)):
                if mot1[i] != mot2[i]:
                    if mot1[i] not in self._alphabet:
                        self._alphabet.append(mot1[i])
                    if mot2[i] not in self._alphabet:
                        self._alphabet.append(mot2[i])
                if mot1[i] == mot2[i]:
                    if mot1[i] not in self._alphabet:
                        self._alphabet.append(mot1[i])


if __name__ == "__main__":
    test = alphabet([1, 2, 3, 4, 8, 9, 7])
    print(test.compare(49, 57))


relation = {
    a: [b, c, g, h, i],
    b: [c, g, h, i, j],
    c: [],
    d: [f, g, h, i, j],
    e: [f, g, h, i, j],
    f: [g, h, i, j],
    g: [h, i, j],
    h: [i, j],
    i: [],
    j: [],
}
