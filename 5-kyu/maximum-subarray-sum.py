"""
DESCRIPTION:
The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]
Easy case is when the list is made up of only positive numbers and the maximum sum is the sum of the whole array. If the list is made up of only negative numbers, return 0 instead.

Empty list is considered to have zero greatest sum. Note that the empty list or array is also a valid sublist/subarray.
"""


def max_sequence(arr: list):
    iter_items = iter(arr)
    try:
        temp_sum = next(iter_items)
        print("temp_sum: %o" % (temp_sum))
    except StopIteration:
        temp_sum = 0
    max_sum = temp_sum
    for item in iter_items:
        temp_sum = max(temp_sum + item, item)
        max_sum = max(temp_sum, max_sum)
    return max(max_sum, 0)


print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_sequence([0, -1, -2, -3]))


def max_sequence_v2(arr: list):
    return max(
        [sum(arr[i:j]) for i in range(len(arr) + 1) for j in range(len(arr) + 1)]
    )


print(max_sequence_v2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
