"""
Complete the function which converts hex number (given as a string) to a decimal number.
"""


def hex_to_dec(s: str) -> int:
    return int(s, 16)


print(hex_to_dec("10"))
print(hex_to_dec("0xA"))
