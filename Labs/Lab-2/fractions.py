""" LAB 02 - 01/17/23
Fractions - Sterling Miller
"""


class Fraction:
    """ Class that create a fraction object """
    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den
        self.simplify()

        if self.num < 0:
            raise ValueError("Denominator cannot be 0 and Numerator cannot be negative")
        elif self.den <= 0:
            raise ValueError("Denominator cannot be 0 and Numerator cannot be negative")

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __mul__(self, other: "Fraction"):
        return Fraction(self.num * other.num, self.den * other.den)

    def __add__(self, other: "Fraction"):
        return Fraction((self.num * other.den) + (other.num * self.den), (self.den * other.den))

    def simplify(self):
        my_gcd = gcd(self.num, self.den)
        self.num //= my_gcd
        self.den //= my_gcd


def gcd(a: int, b: int) -> int:
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a
