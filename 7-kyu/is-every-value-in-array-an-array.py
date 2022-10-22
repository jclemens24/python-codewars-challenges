"""
DESCRIPTION:
Is every value in the array an array?

This should only test the second array dimension of the array. The values of the nested arrays don't have to be arrays.

Examples:

[[1],[2]] => true
['1','2'] => false
[{1:1},{2:2}] => false
"""


def arr_check(arr: list):
    list_flag = False
    for item in arr:
        list_flag = bool(isinstance(item, list))

    return list_flag


print(arr_check([[1], [2]]))
