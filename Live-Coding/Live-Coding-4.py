""" Live Coding #4 - 01/26/2023 """
""" Many Foods are Recursive """


class Food:
    """ Abstract Class to make Food Object """
    def count_calories(self) -> int:
        raise AssertionError("Must specify type of food")

    def print_recipe(self):
        raise AssertionError("Must specify food to get recipe")


class BaseIngredient(Food):
    """ Base Ingredients i.e. flour, salt, eggs, etc. """
    def __init__(self, name: str, calories: int):
        self.name = name
        self.calories = calories

    def count_calories(self) -> int:
        return self.calories

    def print_recipe(self, level: int = 0):
        indent = "   " * level
        print(f'{indent}{self.name}: {self.count_calories} calories')


class CompositeFood(Food):
    """ List of Ingredients Food is made of i.e. Pizza """
    def __init__(self, name: str, ingredients: list[Food]):
        self.name = name
        self.ingredients = ingredients

    def count_calories(self) -> int:
        total_calories = 0
        for i in self.ingredients:
            total_calories += i.count_calories()
        return total_calories

    def print_recipe(self, level: int = 0):
        indent = "   " * level
        print(f'{indent}{self.name}: {self.count_calories} calories')
        for item in self.ingredients:
            item.print_recipe(level+1)


def main():
    """ Building Pizza """
    ''' Pizza Crust '''
    flour = BaseIngredient('flour', 20)
    salt = BaseIngredient('salt', 0)
    yeast = BaseIngredient('yeast', 3)
    sugar = BaseIngredient('sugar', 18)
    crust = CompositeFood('crust', [flour, salt, yeast, sugar])
    ''' Pizza Sauce '''
    tomato = BaseIngredient('tomatoes', 50)
    oregano = BaseIngredient('oregano', 1)
    tyme = BaseIngredient('tyme', 1)
    basil = BaseIngredient('basil', 1)
    sauce = CompositeFood('sauce', [tomato, oregano, tyme, basil])
    ''' Pizza Toppings '''
    cheese = BaseIngredient('mozzarella', 120)
    pineapple = BaseIngredient('pineapple', 80)
    anchovies = BaseIngredient('anchovies', 99)
    toppings = CompositeFood('toppings', [cheese, pineapple, anchovies])
    ''' Create Pizza '''
    pizza = CompositeFood('pizza', [crust, sauce, toppings])
    print(f'This pizza has {pizza.count_calories()} calories.')
    pizza.print_recipe()


if __name__ == '__main__':
    main()
