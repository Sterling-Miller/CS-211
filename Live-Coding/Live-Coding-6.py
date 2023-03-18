""" Live Coding #6 - 02/16/2023 """
instr = 0b01101111

opcodes = {
    0b000: "ORA",
    0b001: "AND",
    0b011: "ADC"
}


def opcode(i: int) -> str:
    op = (i >> 5) & 7
    return opcodes[op]


print(opcode(instr))
