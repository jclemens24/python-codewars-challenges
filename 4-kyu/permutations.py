"""
DESCRIPTION:
In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

Examples:

* With input 'a'
* Your function should return: ['a']
* With input 'ab'
* Your function should return ['ab', 'ba']
* With input 'aabb'
* Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
The order of the permutations doesn't matter.
"""

from itertools import permutations as perm


def permutations_func(s: str):
    mylist = ["".join(element) for element in list(perm(s))]
    return list(dict.fromkeys(mylist))


print(permutations_func("ab"))
print(permutations_func("aabb"))

# A set makes a little more sense in this situation because we want unique
# values


def permutations_v2(s: str):
    return list("".join(el) for el in set(perm(s)))


print(permutations_v2("ab"))
print(permutations_v2("aabb"))
