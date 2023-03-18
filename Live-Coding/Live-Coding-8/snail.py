"""Snail graphics are slower and simpler than turtle graphics, but
they have one nice feature:  A sequence of snail graphics commands
can be encoded as hexadecimal numbers, a format we call
"snail language you might enjoy", or "slyme".
"""

import slate
from slate import Slate
from typing import List

# slyme format 8-bit encoding:
# bit 7:  0 = move, 1 = draw
# bits bits 3..6: distance, 0..15 steps
# bits 0..2:  direction index


def inked(cmd: int) -> bool:        # FixMe
    """Extract the inked/uninked bit from integer command"""
    bit = cmd >> 7
    return bool(bit)


def direction(cmd: int) -> slate.Dir:       # FixMe
    """Extract the direction indicator from integer command"""
    dir_bit = cmd & 7
    return slate.Dir(dir_bit)


def dist(cmd: int) -> int:      # FixMe
    """Extract the distance (number of steps) from integer command"""
    cmd = (cmd >> 3) & 15
    return cmd


class Snail:
    """Snails can interpret Slyme code to draw character graphic on a slate"""
    def __init__(self):
        self.slate = Slate()

    def interpret(self, commands: List[str]):
        """Each string in 'commands' is two hexadecimal digits"""
        for command in commands:
            cmd_int = int(command, base=16)
            vec = direction(cmd_int)
            steps = dist(cmd_int)
            self.slate.stroke(vec, steps, inked(cmd_int))


def example():
    # Ring
    snail = Snail()
    commands = slate.ox_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()
    # Z
    snail = Snail()
    commands = slate.z_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()
    # S
    snail = Snail()
    commands = slate.s_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()
    # concentric
    snail = Snail()
    commands = slate.concentric_example()
    print(commands)
    snail.interpret(commands)
    print(snail.slate)
    print()


def main():
    example()


if __name__ == "__main__":
    main()
