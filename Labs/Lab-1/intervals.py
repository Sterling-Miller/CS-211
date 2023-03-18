"""Closed intervals of integers
Sterling Miller, 2023-01-10, CIS 211
"""


class Interval:
    """ An interval m..n represents the set of intervals at least m and at most n. """
    def __init__(self, low: int, high: int):
        """ Interval(low, high) is the interval low..high """
        # assert low < high
        if low > high:
            raise ValueError("Low must be less than High")
        self.low = low
        self.high = high

    def __eq__(self, other: "Interval") -> bool:
        """ Intervals are equal if they have the same low and high bounds """
        return (self.low == other.low) and (self.high == other.high)

    def __str__(self) -> str:
        """ Printed Representation """
        return f"({self.low}, {self.high})"

    def __repr__(self) -> str:
        """ Debugging / Console Representation """
        return f"Interval({self.low}, {self.high})"

    def contains(self, i: int) -> bool:
        """ Integer i is within the closed interval """
        return (i >= self.low) and (i <= self.high)

    def overlaps(self, other: "Interval") -> bool:
        """ i.overlaps(j) if i and j have some elements in common """
        if self.high < other.low:
            return False
        if self.low > other.high:
            return False
        return True

    def join(self, other: "Interval") -> "Interval":
        """ Create a new Interval that contains the union of elements in self and other.
        Precondition: self and other must overlap. """
        assert (self.overlaps(other))
        small = min(self.low, other.low)
        big = max(self.high, other.high)
        return Interval(small, big)
