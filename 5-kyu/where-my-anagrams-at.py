"""
DESCRIPTION:
What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
"""
from collections import Counter


def anagrams(word: str, words: list[str]) -> list:
    result = [string for string in words if sorted(string) == sorted(word)]
    return result


print(anagrams("abba", ["aabb", "abcd", "bbaa", "dada"]))


def anagrams_v2(word: str, words: list[str]) -> list:
    og = Counter(word)
    return [string for string in words if Counter(string) == og]


print(anagrams_v2("abba", ["aabb", "abcd", "bbaa", "dada"]))


def anagrams_v3(word: str, words: list[str]) -> list:
    letter = {x: word.count(x) for x in word}
    result = []
    for w in words:
        letters = {x: w.count(x) for x in w}
        if letters == letter:
            result.append(w)
    return result


print(anagrams_v3("abba", ["aabb", "abcd", "bbaa", "dada"]))
