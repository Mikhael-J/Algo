class Pile:
    def __init__(self) -> None:
        super().__init__()
        self.pile = []

    def puch(self, i: any) -> None:
        self.pile.append(i)

    def remove(self) -> None:
        self.pile.pop()

    def size(self) -> int:
        return len(self.pile)

    def get_remove_Last(self) -> any:
        last = self.last()
        self.remove()
        return last

    def empty(self) -> bool:
        return self.pile == []

    def last(self) -> any:
        return self.pile[-1]

    def get(self):
        return self.pile
