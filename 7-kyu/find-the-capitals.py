"""
DESCRIPTION:
Instructions
Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.

Example
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );
"""


def capitals(word: str) -> list[int]:

    return [i for i, char in enumerate(word) if char.isupper()]


print(capitals("CodEWaRs"))


def capitals_v2(word):
    return filter(lambda x: word[x].isupper(), range(len(word)))


print(capitals_v2("CodEWaRs"))
