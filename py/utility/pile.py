class Pile:
    def __init__(self):
        super().__init__()
        self.pile = []

    def add(self, i):
        self.pile.append(i)

    def remove(self):
        self.pile.pop()

    def size(self):
        return len(self.pile)

    def getPile(self):
        return self.pile

    def get_remove_Last(self):
        last = self.pile[len(self.pile)-1]
        self.remove()
        return last

    def somme(self):
        res = 0
        for i in self.pile:
            res = i + res
        return res

