""" LAB 09 - 03/07/23
Creatures - Sterling Miller
"""


class Creature(object):
    """ Abstract Class used to create Orthrus, Cerberus, and Head """

    def __init__(self):
        raise NotImplementedError("Abstract classes should not be instanciated")

    def __str__(self) -> str:
        raise NotImplementedError("Abstract class methods should not be called")

    def search(self, value: str) -> bool:
        raise NotImplementedError("Abstract class methods should not be called")


class Orthrus(Creature):

    def __init__(self, left: Creature, right: Creature):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left} {self.right}"

    def search(self, name: str) -> bool:
        return self.left.search(name) or self.right.search(name)


class Cerberus(Creature):

    def __init__(self, left: Creature, middle: Creature, right: Creature):
        self.left = left
        self.mid = middle
        self.right = right

    def __str__(self):
        return f"{self.left} {self.mid} {self.right}"

    def search(self, name: str) -> bool:
        return self.left.search(name) or self.mid.search(name) or self.right.search(name)


class Head(Creature):

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def search(self, name: str) -> bool:
        return self.name == name


def main():
    doggy1 = Head("Kane")
    doggy2 = Head("Wolfie")
    doggy3 = Head("Rugal")
    doggy4 = Head("Taker")
    ort1 = Orthrus(doggy1, doggy2)
    ort2 = Orthrus(doggy3, Head("Jeff"))
    cer = Cerberus(ort1, doggy4, ort2)

    assert cer.search("Kane")
    assert cer.search("Jeff")
    assert not cer.search("Scooter")
    assert ort2.search("Rugal")
    assert ort1.search("Wolfie")
    assert not ort2.search("Scooter")
    print("Passes assertions")


if __name__ == '__main__':
    main()
