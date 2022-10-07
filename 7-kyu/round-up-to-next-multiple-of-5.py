"""
DESCRIPTION:
Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?

Examples:

input:    output:
0    ->   0
2    ->   5
3    ->   5
12   ->   15
21   ->   25
30   ->   30
-2   ->   0
-5   ->   -5
etc.
Input may be any positive or negative integer (including 0).

You can assume that all inputs are valid integers.
"""

# This is a brute force solution
def round_to_next5(n: int) -> int:
    if n % 5 == 0:
        return n
    output = 0
    for i in range(n, n + 5):
        if i % 5 == 0:
            output = i
        else:
            continue
    return output


print(round_to_next5(0))
print(round_to_next5(2))
print(round_to_next5(3))
print(round_to_next5(12))
print(round_to_next5(21))
print(round_to_next5(30))
print(round_to_next5(-2))
print(round_to_next5(-5))


def round_to_next5_v2(n: int) -> int:
    return n + (5 - n) % 5


print(round_to_next5_v2(0))
print(round_to_next5_v2(2))
print(round_to_next5_v2(3))
print(round_to_next5_v2(12))
print(round_to_next5_v2(21))
print(round_to_next5_v2(30))
print(round_to_next5_v2(-2))
print(round_to_next5_v2(-5))
