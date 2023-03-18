""" Live Coding #2 - 01/17/2023 """
"""CONVERSIONS/CURRENCY"""


class Currency:
    """Abstract base class"""

    def __init__(self):
        raise NotImplementedError("Don't! You aren't able to make-up a Currency")
        self.conversion_rate = 1.0
        self.symbol = "<NO CURRENCY>"

    def __str__(self) -> str:
        return self.symbol

    def convert(self, other: "Currency", amount: float):
        return amount * self.conversion_rate / other.conversion_rate


class Dollar(Currency):
    """Concreate class that you can make objects (Dolllars) from"""
    def __init__(self, conversion: float):
        self.conversion_rate = conversion
        self.symbol = "$"


class Euro(Currency):
    """Concreate class that you can make objects (Euros) from"""
    def __init__(self, conversion: float):
        self.conversion_rate = conversion
        self.symbol = "€"


class Cash:

    def __init__(self, amt: float, currency: Currency):
        self.amt = amt
        self.currency = currency

    def __str__(self):
        return f"{self.currency.symbol}{round(self.amt, 2)}"

    def convert_to(self, currency: Currency) -> "Cash":
        self.amt = self.currency.convert(currency, self.amt)
        self.currency = currency


"""ANIMALS"""


class Animal:

    def __init__(self):
        raise NotImplementedError("No Generic Animals")
        self.name = "<NO NAME>"

    def voice(self) -> str:
        raise NotImplementedError("No Generic Animal Sounds")

    def speak(self):
        print(f"{self.name} says '{self.voice()}'")


class Dog(Animal):
    def __init__(self, name: str):
        self.name = name

    def voice(self) -> str:
        return "WOOF WOOF"


class Cat(Animal):
    def __init__(self, name: str):
        self.name = name

    def voice(self) -> str:
        return "MEOW"


def main():
    """CONVERSIONS/CURRENCY"""
    dollars = Dollar(1.0)
    euros = Euro(1.1)
    print(dollars.convert(euros, 100))

    wallet = Cash(100, euros)
    print(f"I start with {wallet}")
    wallet.convert_to(dollars)
    print(f"Now I have {wallet}")

    """ANIMALS"""
    merlin = Dog("Merlin")
    nora = Cat("Nora")
    pets = [merlin, nora]
    for pet in pets:
        pet.speak()


if __name__ == '__main__':
    main()
