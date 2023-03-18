""" LAB 03 - 01/24/23
Shape3D - Sterling Miller
"""
import math


class Shape3D:
    """ Abstract class for creating shapes """
    def __init__(self):
        raise NotImplementedError("Abstract class cannot be instantiated")

    def volume(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def area(self) -> float:
        raise NotImplementedError("Not implemented for abstract class")

    def print_info(self):
        return f"Area: {self.area()}, Volume: {self.volume()}"


class Cylinder(Shape3D):
    """ Class that makes a cylinder """
    def __init__(self, radius: float, height: float):
        self.rad = radius
        self.height = height

    def volume(self) -> float:
        return math.pi * (self.rad * self.rad) * self.height

    def area(self) -> float:
        return (2 * math.pi * (self.rad * self.rad)) + (2 * math.pi * self.rad * self.height)


class Cuboid(Shape3D):
    """ abstract class that creates rectangles """
    def __init__(self, width: float, length: float, height: float):
        self.width = width
        self.length = length
        self.height = height

    def volume(self) -> float:
        return self.width * self.length * self. height

    def area(self) -> float:
        return (2 * self.width * self.length) + (2 * self.width * self.height) + (2 * self.length * self.height)


class Cube(Cuboid):
    """ Subclass of Cuboid that creates a perfect cube """
    def __init__(self, width: float):
        super().__init__(width, width, width)


def main():
    cyl = Cylinder(3, 5)
    cuboid = Cuboid(6, 4, 9)
    lst = [Cube(3), cyl, cuboid]
    for shape in lst:
        print(shape.print_info())


if __name__ == '__main__':
    main()
