"""
DESCRIPTION:
In some countries of former Soviet Union there was a belief about lucky tickets. A transport ticket of any sort was believed to posess luck if sum of digits on the left half of its number was equal to the sum of digits on the right half. Here are examples of such numbers:

003111    #             3 = 1 + 1 + 1
813372    #     8 + 1 + 3 = 3 + 7 + 2
17935     #         1 + 7 = 3 + 5  // if the length is odd, you should ignore the middle number when adding the halves.
56328116  # 5 + 6 + 3 + 2 = 8 + 1 + 1 + 6
Such tickets were either eaten after being used or collected for bragging rights.

Your task is to write a funtion luck_check(str), which returns true/True if argument is string decimal representation of a lucky ticket number, or false/False for all other numbers. It should throw errors for empty strings or strings which don't represent a decimal number.
"""
from operator import eq


def luck_check(string: str) -> bool:
    if not string or not string.isdigit():
        raise ValueError
    left, right, total = 0, len(string) - 1, 0
    while left != right and left < right:
        total += int(string[left]) - int(string[right])
        left += 1
        right -= 1
    return eq(total, 0)


print(luck_check("003111"))


def luck_check_v2(string: str) -> bool:
    if not string or not string.isnumeric():
        raise ValueError
    return not sum(
        int(left) - int(right)
        for left, right in zip(string[: len(string) // 2], string[::-1])
    )


print(luck_check_v2("003111"))
