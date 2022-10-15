"""
DESCRIPTION:
write me a function stringy that takes a size and returns a string of alternating '1s' and '0s'.

the string should start with a 1.

a string with size 6 should return :'101010'.

with size 4 should return : '1010'.

with size 12 should return : '101010101010'.

The size will always be positive and will only use whole numbers.
"""


def stringy(size: int) -> str:
    if size % 2 == 0:
        new_size = size / 2
        return "10" * new_size
    return "".join(["1" if i % 2 == 0 else "0" for i in range(0, size)])


print(stringy(6))
print(stringy(5))


def stringy_v2(size: int) -> str:
    return ("10" * size)[:size]


print(stringy_v2(6))
print(stringy_v2(5))
