"""Mini-exam 3 (on Canvas), CS 211 @ uoregon, Winter 2023

Problem 1 is a binary decoding (unpacking) problem.  The method you must write is called set_tile.
It extracts two three-bit unsigned integer fields from an integer, to use as a row and column
index in a grid.  Problem 2 is a recursive search in an ordered binary tree of intervals.

List of methods and functions to complete:
- set_tile (in problem 1, class Board)
- max (in problem 2, class Inner)
- contains (in problem 2, class Inner)

Detailed instructions are in comments.
"""
####
# Problem 1
# 'Board' contains a 8x8 grid of Tile objects, each of which holds
# a string.  The row and column indexes for method 'set_tile' are
# 3 bit fields packed into a single integer by 'encode_position'.
#
# Complete method set_tile.  For full credit, your code should be short
# (4 lines or fewer), readable, and efficient.  It should not use the `bin`
# function.
#####
EMPTY = " "          # String indicating an emtpy tile


def encode_position(row_num, col_num) -> int:
    """Encode row and column of a grid location into
    an integer as two 3-bit fields, row in bits 3..5
    and column in bits 0..3
    """
    assert 0 <= row_num < 8
    assert 0 <= col_num < 8
    return ((row_num & 7) << 3) | (col_num & 7)


class Tile:
    """A tile holds a game piece, represented as a string.
    A single space designates an empty tile.
    """
    def __init__(self, game_piece=" "):
        self._piece = game_piece

    def set(self, value: str):
        self._piece = value

    def __str__(self) -> str:
        return self._piece

    def __repr__(self) -> str:
        return f"Tile({repr(self._piece)})"


class Board:
    """A 8x8 board on which each Tile contains a string"""
    def __init__(self):
        self._tiles: list[list[Tile]] = []
        for row_i in range(8):
            row = []
            for col_i in range(8):
                row.append(Tile(EMPTY))
            self._tiles.append(row)

    def set_tile(self, index: int, label: str):
        """Set the tile at the encoded position to label"""
        row_index = (index >> 3) & 7
        col_index = index & 7
        self._tiles[row_index][col_index].set(label)    # FIXME -- use the index

    def __str__(self):
        """Printed form is a multi-line string"""
        row_strs = []
        for row in self._tiles:
            row_strs.append("".join(str(t) for t in row))
        return "\n".join(row_strs)


# Test case:
# ABCDEFGH diagonal upper left to lower right,
# STUVWXYZ diagonal upper right to lower left
b = Board()
for i, ch in enumerate("ABCDEFGH"):
    diag = encode_position(i, i)
    b.set_tile(diag, ch)
for i, ch in enumerate("STUVWXYZ"):
    cross = encode_position(i, 7-i)
    b.set_tile(cross, ch)

print(b)
assert str(b) == """
A      S
 B    T 
  C  U  
   DV   
   WE   
  X  F  
 Y    G 
Z      H
""".strip()
print("Passed problem 1")


###
#  Problem 2:
#  An ordered binary tree of disjoint integer intervals.
#
# A disjoint interval tree contains an ordered,
# disjoint set of numeric intervals, like 1-3. At each
# internal node, all the intervals in the left child are
# less than all the intervals in the right child.
# You must finish methods 'max' and 'contains' of class Inner.
#
# You can receive partial credit for a solution that works, even
# if it is inefficient.  For full credit, 'max' and 'contains'
# should be efficient, with cost proportional to the height of
# the tree (the distance from the root to a leaf) rather than the
# total size of the tree.
#
# Efficient solutions are possible because
# we know the tree is ordered and the intervals are disjoint:
# The largest element contained by any interval in the left subtree
# is less than the smallest element contained by any interval in the
# right subtree.
###
class Intervals:
    """Abstract base class"""
    def contains(self, i: int) -> bool:
        """Does i belong to any interval in this tree?"""
        raise NotImplementedError(f"class {self.__class__.__name__} hasn't implemented 'contains'")

    def max(self) -> int:
        """Maximum value in any interval in this tree"""
        raise NotImplementedError(f"class {self.__class__.__name__} hasn't implemented 'max'")


class Inner(Intervals):
    def __init__(self, left: Intervals, right: Intervals):
        self.left = left
        self.right = right
        # Use order of intervals to search quickly
        self.split = self.left.max()

    def max(self) -> int:
        left = self.left.max()
        right = self.right.max()
        return max(left, right)    # FIXME

    def contains(self, i: int) -> bool:
        if self.right.contains(i) or self.left.contains(i):
            return True
        return False  # FIXME


class Leaf(Intervals):
    def __init__(self, low: int, high: int):
        assert low <= high
        self.low = low
        self.high = high

    def max(self) -> int:
        return self.high

    def contains(self, i: int) -> bool:
        return self.low <= i <= self.high


intervals = Inner(Leaf(-20, -10), Inner(Leaf(0, 10), Leaf(20, 30)))
assert intervals.max() == 30
assert intervals.contains(-15)
assert intervals.contains(0)
assert intervals.contains(8)
assert intervals.contains(25)
assert not intervals.contains(-30)
assert not intervals.contains(-5)
assert not intervals.contains(35)
print("Passed Intervals Tests")
