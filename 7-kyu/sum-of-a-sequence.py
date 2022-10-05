"""
Your task is to make function, which returns the sum of a sequence of integers.

The sequence is defined by 3 non-negative values: begin, end, step (inclusive).

If begin value is greater than the end, function should returns 0

Examples

2,2,2 --> 2
2,6,2 --> 12 (2 + 4 + 6)
1,5,1 --> 15 (1 + 2 + 3 + 4 + 5)
1,5,3  --> 5 (1 + 4)
"""


def sequence_sum(begin_number, end_number, step):
    if begin_number > end_number:
        return 0
    result = 0

    for i in range(begin_number, end_number + 1, step):
        result += i
    return result


print(sequence_sum(2, 2, 2))
print(sequence_sum(2, 6, 2))


def sequence_sum_v2(begin, end, step) -> int:
    return sum(range(begin, end + 1, step))


print(sequence_sum_v2(2, 2, 2))
print(sequence_sum_v2(2, 6, 2))

# Using pure mathematical concepts
# This is how I would have solved in JavaScript


def sequence_sum_v3(begin, end, step):
    num = (end - begin) // step
    return (1 + num) * (begin + step * num / 2) if begin <= end else 0


print(sequence_sum_v3(2, 2, 2))
print(sequence_sum_v3(2, 6, 2))
