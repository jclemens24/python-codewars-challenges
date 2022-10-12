"""
DESCRIPTION:
You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3
"""
from collections import Counter


def stray(arr: list[int]) -> int:
    count = Counter(arr)
    for key in count:
        if count[key] == 1:
            return key
    return -1


print(stray([1, 1, 1, 1, 1, 1, 2]))


def stray_v2(arr):
    for num in arr:
        if arr.count(num) == 1:
            return num
    return -1


print(stray_v2([1, 1, 1, 1, 1, 1, 2]))


def stray_v3(arr: list[int]) -> int:
    return min(arr, key=arr.count)


print(stray_v3([1, 1, 1, 1, 1, 1, 2]))
