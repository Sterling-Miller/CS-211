""" Live Coding #9 - 03/7/2023 """

HEX_DICT: dict = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
REV_HEX: str = '0123456789ABCDEF'


def hex_to_binary(int_str: str) -> int:
    """ Takes in hex string and returns equivalent integer in binary """
    ret_num = 0
    for char in int_str:
        ret_num = ret_num << 4
        ret_num |= HEX_DICT[char]
    return ret_num


def binary_to_hex(int_str: int) -> str:
    """ Takes in binary string and returns equivalent integer in hex """
    mask = 0b1111
    ret_str = ''
    # if int_str == 0:
    #     return '0'
    # neg = False
    # if int_str < 0:
    #     int_str = abs(int_str)
    #     neg = True
    while int_str > 0:
        new_digit = int_str & mask
        ret_str = REV_HEX[new_digit] + ret_str
        int_str = int_str >> 4
    return ret_str


def is_two_phase(l: list[int]) -> bool:
    """ Checks whether l first increases, then decreases """
    increasing = True
    for n in range(1, len(l)):
        if l[n] > l[n - 1]:
            if not increasing:
                return False

        if l[n] < l[n - 1]:
            increasing = False

    return True


def main():
    gud = [0, 0, 1, 2, 3, 4, 4, 4, 3, 2, 1, 0]
    bud = [0, 0, 1, 2, 3, 4, 3, 2, 3, 4, 2, 0]
    assert hex_to_binary('B4')
    assert binary_to_hex(10111001)
    assert is_two_phase(gud)
    assert not is_two_phase(bud)
    print('Everything passes')


if __name__ == '__main__':
    main()
