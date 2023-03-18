""" Live Coding #5 - 02/2/2023 """
"""Hybrid fruit trees ... all your favorites from one tree"""


class FruitTree:
    """Abstract base class for fruit trees"""

    def count(self, kind: str) -> int:
        """How much fruit of a particular kind is in the tree?"""
        raise NotImplementedError(f"{self.__class__.__name__} has not implemented count")

    def only(self, kind) -> bool:
        """ Is a Tree Entirely Made-Up of a Single Fruit? """
        raise NotImplementedError(f"{self.__class__.__name__} has not implemented only")


class BinaryBranch(FruitTree):
    """An internal node in the tree, with exactly two children"""

    def __init__(self, left: FruitTree, right: FruitTree):
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.left}, {self.right}"

    def count(self, kind: str) -> int:
        return self.left.count(kind) + self.right.count(kind)

    def only(self, kind: str) -> bool:
        return self.left.only(kind) and self.right.only(kind)


class NaryBranch(FruitTree):
    """An inner node with zero or more children"""

    def __init__(self):
        self.children: list[FruitTree] = []

    def append(self, child: FruitTree):
        self.children.append(child)

    def count(self, kind: str) -> int:
        ttl = 0
        for child in self.children:
            ttl += child.count(kind)
        return ttl

    def only(self, kind: str) -> bool:
        for child in self.children:
            if not child.only(kind):
                return False
        return True


class Apple(FruitTree):
    """A leaf node bearing fruit, in this case a single apple."""

    def __init__(self):
        pass

    def __str__(self):
        return "A"

    def count(self, kind: str) -> int:
        if kind == 'apple':
            return 1
        return 0

    def only(self, kind: str) -> bool:
        return kind == 'apple'


class Pear(FruitTree):

    def __init__(self):
        pass

    def __str__(self):
        return "A"

    def count(self, kind: str) -> int:
        if kind == 'pear':
            return 1
        return 0

    def only(self, kind: str) -> bool:
        return kind == 'pear'


def from_postfix(s: str) -> FruitTree:
    parts = s.split()
    stack = []
    for part in parts:
        if part == 'A':
            stack.append(Apple())
        if part == 'P':
            stack.append(Pear())
        if part == '+':
            right = stack.pop()
            left = stack.pop()
            stack.append(BinaryBranch(left, right))
    return stack[0]


# Test cases
tree = NaryBranch()
tree.append(BinaryBranch(Apple(), BinaryBranch(Apple(), Pear())))
assert tree.count("apple") == 2
assert tree.count("pear") == 1
tree2 = NaryBranch()
tree2.append(BinaryBranch(Apple(), BinaryBranch(Apple(), Apple())))
assert tree2.only('apple') is True
assert tree2.only('pear') is False
tree3 = from_postfix('A A + P P + +')
print(tree3)
print("Done.")
