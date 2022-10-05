"""
DESCRIPTION:
The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""
from collections import Counter


def count(string: str):
    if len(string) is None:
        return {}
    c = Counter(string)
    return dict(c)


print(count("aba"))
print(count(""))


def count_v2(string: str):
    return {i: string.count(i) for i in string}


print(count_v2("aba"))

# Using a simple dict


def count_v3(string):
    instances = {}
    for char in string:
        instances[char] = instances.get(char, 0) + 1
    return instances


print(count_v3("aba"))
