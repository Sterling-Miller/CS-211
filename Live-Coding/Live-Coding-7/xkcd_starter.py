"""XKCD Regex detective.

Your mission, if you choose to accept it, is
to find and print all the addresses in
clues.txt
"""
import re

# Starter pattern is any string of digits.
# 1  First implementation: \b[0-9].*(Ave | Street | Lane | [A-Z][A-Z])
CLUE_PATTERN = re.compile(r"""
[0-9]+.+([A-Z]+[a-z]* | [A-Z][A-Z])  # match any string of digits
""", re.VERBOSE)

# 1  First implementation: \b\S+@\S+\b
# 2  Second implementation: \b\S+@.*(.com | .net | .org | .stars)
# 3  Third implementation: \b\S+@.(\.*\w)+
EMAIL_PATTERN = re.compile(r"""
\b\S+@.*(.com | .net | .org | .stars)  # match any string of digits
""", re.VERBOSE)


def get_a_clue(s: str):
    """Print any addresses found in s"""
    for match in re.finditer(CLUE_PATTERN, s):
        print(match.group(0))


def scan_file(filename: str):
    """Look for clues in a file"""
    f = open(filename)
    for line in f:
        get_a_clue(line)


if __name__ == "__main__":
    scan_file("clues.txt")
