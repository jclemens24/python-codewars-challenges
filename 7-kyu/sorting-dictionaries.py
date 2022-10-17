"""
DESCRIPTION:
Python dictionaries are inherently unsorted. So what do you do if you need to sort the contents of a dictionary?

Create a function that returns a sorted list of (key, value) tuples (Javascript: arrays of 2 items).

The list must be sorted by the value and be sorted largest to smallest.

Examples
sort_dict({3:1, 2:2, 1:3}) == [(1,3), (2,2), (3,1)]
sort_dict({1:2, 2:4, 3:6}) == [(3,6), (2,4), (1,2)]
"""
from operator import itemgetter


def sort_dict(d: dict) -> list:
    my_list = sorted(list(d.items()), key=lambda ele: ele[1], reverse=True)
    return my_list


print(sort_dict({3: 1, 2: 2, 1: 3}))
print(sort_dict({1: 2, 2: 4, 3: 6}))


def sort_dict_v2(d: dict) -> list:
    return sorted(d.items(), key=itemgetter(1), reverse=True)


print(sort_dict_v2({3: 1, 2: 2, 1: 3}))
print(sort_dict_v2({1: 2, 2: 4, 3: 6}))
