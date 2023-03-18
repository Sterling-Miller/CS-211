"""Mini-Project: Sweeping a List
Sterling Miller, 2023-01-11, CIS 211
"""


def all_same(l: list) -> bool:
    """A function that determines whether
    all the elements in a list are the same"""
    if len(l) > 0:
        letter = l[0]
        for item in l:
            if letter != item:
                return False
            else:
                letter = item
    return True


def dedup(l: list) -> list:
    """A function that returns a de-duplicated
    version of the input list"""
    condensed = []
    for item in l:
        if item not in condensed:
            condensed.append(item)
    return condensed


def max_run(l: list) -> int:
    """A function that determines the longest
    subsequence with identical values"""
    if len(l) > 1:
        num = l[0]
        parsing = []
        largest = []
        for item in l:
            if item == num:
                parsing.append(item)
                num = item
            else:
                if largest < parsing:
                    largest = parsing
                    parsing = []
                    num = item
                    parsing.append(item)
        return len(largest)
    return len(l)