""" LAB 06 - 02/14/23
Binary Number - Sterling Miller
"""


class BinaryNumber:

    def __init__(self, bits: list[int]):
        self.bits = bits

    def __str__(self):
        return f'{self.bits}'

    def __or__(self, other) -> 'BinaryNumber':
        bitArray = []
        for num in self.bits:
            for bit in other.bits:
                if num == 0 and bit == 0:
                    bitArray.append(0)
                else:
                    bitArray.append(1)
        return BinaryNumber(bitArray)

    def __and__(self, other) -> 'BinaryNumber':
        bitArray = []
        for num in self.bits:
            for bit in other.bits:
                if num == 1 and bit == 1:
                    bitArray.append(1)
                else:
                    bitArray.append(0)
        return BinaryNumber(bitArray)

    def left_shift(self):
        self.bits[:-1] = self.bits[1:]
        self.bits[-1] = 0

    def right_shift(self):
        self.bits[1:] = self.bits[:-1]
        self.bits[0] = 0

    def extract(self, start: int, end: int) -> list[int]:
        assert 0 <= start < end
        assert start < end <= len(self.bits)

        bitArray = [0] * len(self.bits)
        left = (len(self.bits) - 1) - end
        right = (len(self.bits) - 1) - start

        for i in range(left, right + 1):
            bitArray[i] = 1
        b1 = BinaryNumber(bitArray)

        b2 = b1 & self
        for i in range(start):
            b2.right_shift()
        return


bn = BinaryNumber([1, 0, 1, 0, 1])
bn2 = BinaryNumber([1, 1, 1, 0, 0])
bn.left_shift()
bn2.right_shift()
bn = BinaryNumber([1, 0, 0, 1, 0, 1, 1, 1])
extracted = bn.extract(2, 4)
