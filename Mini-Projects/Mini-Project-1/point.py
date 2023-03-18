"""Mini-Project: Point
Sterling Miller, 2023-01-11, CIS 211
"""


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other: "Point") -> bool:
        """Determines if Points are Equal"""
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self) -> str:
        """Printed Representation"""
        return f"({self.x}, {self.y})"

    def move(self, dx: int, dy: int):
        """Moves Point"""
        self.x = self.x + dx
        self.y = self.y + dy
