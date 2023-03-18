""" Live Coding #1 - 01/10/2023 & 01/12/2023 """
import plot from canvas


class Point:
    """A Coordinate pair (x, y)"""
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """Printed Representation"""
        return f"({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        """Debugging / Console Representation"""
        return f"Point({self.x}, {self.y})"

    def move(self, other: "Point") -> "Point":
        return Point(self.x + other.x, self.y + other.y)

    def move_to(self, new_x: int, new_y: int):
        self.x = new_x
        self.y = new_y


class Rect:
    def __init__(self, ll: Point, ur: Point):
        """Rectangle defined by lower left and upper right corners"""
        self.ll = ll
        self.ur = ur

    def __add__(self, other: "Rect") -> "Rect":
        """Union of two rectangles is a rectangle that covers both of them"""
        assert isinstance(other, Rect)
        return Rect(Point(min(self.ll.x, other.ll.x), min(self.ll.y, other.ll.y)),
                    Point(max(self.ur.x, other.ur.x), max(self.ur.y, other.ur.y)))

    def draw(self):
        canvas.plot(self.ll.x, self.ll.y, self.ur.x, self.ur.y, color="blue")


def main():
    p = Point(3, 4)
    v = Point(5, 6)
    m = p.move(v)
    assert m.x == 8 and m.y == 10
    print(p, v, m)

    s = Rect(50, 50)


if __name__ == '__main__':
    main()
