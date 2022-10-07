"""
Complete the function scramble(str1, str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
from collections import Counter
from operator import sub


def scramble(s1: str, s2: str) -> bool:
    for char in set(s2):
        if s1.count(char) < s2.count(char):
            return False
    return True


print(scramble("rkqodlw", "world"))


def scramble_v2(s1, s2):
    return len(Counter(s2) - Counter(s1)) == 0


print(scramble_v2("rkqodlw", "world"))


def scramble_v3(s1, s2):
    print(*map(Counter, (s2, s1)))
    return not sub(*map(Counter, (s2, s1)))


print(scramble_v3("rkqodlw", "world"))
