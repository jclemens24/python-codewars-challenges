"""
DESCRIPTION:
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""
from itertools import groupby


def unique_in_order(iterable):
    unique_list = []
    prev = None

    for i in iterable:
        if i != prev:
            unique_list.append(i)
            prev = i
    return unique_list


print(unique_in_order("AAAABBBCCDAABBB"))

# We can also use tools from itertools


def unique_in_order_v2(iterable):
    return [k for (k, _) in groupby(iterable)]


print(unique_in_order_v2("AAAABBBCCDAABBB"))

# Last, we can solve using a lambda and enumerator

unique_in_order_v3 = lambda li: [
    v for k, v in enumerate(li) if k == 0 or li[k - 1] != v
]

print(unique_in_order_v3("AAAABBBCCDAABBB"))
