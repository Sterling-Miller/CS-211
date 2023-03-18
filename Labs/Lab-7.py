""" LAB 07 - 02/21/23
Function Dispatcher - Sterling Miller
"""
import math
from typing import Callable, List


def total_sum(list1: List[int]):
    return sum(list1)


def apply(f: Callable, list1: List[int]):
    list2 = []
    for num in list1:
        list2.append(f(num))
    return list2


def square(list1: List[int]):
    return apply(lambda x: x ** 2, list1)


def magnitude(vector: List[int]):
    return math.sqrt(total_sum(square(vector)))


dispatch_table = {1: total_sum, 2: square, 3: magnitude}


class FunctionDispatcher:

    def __init__(self, dispatch_table: dict):
        self.dispatch_table = dispatch_table

    def process_command(self, key: int, list1: List[int]):
        value = self.dispatch_table[key]
        return value(list1)


if __name__ == '__main__':
    fd = FunctionDispatcher(dispatch_table)
    print(fd.process_command(1, [3, 4]))
    print(fd.process_command(2, [3, 4]))
    print(fd.process_command(3, [3, 4]))
