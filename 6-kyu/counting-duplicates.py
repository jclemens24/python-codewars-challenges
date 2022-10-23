"""
DESCRIPTION:
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
"""
from collections import Counter


def duplicate_count(text: str):
    if text == "" or not text:
        return 0
    p = Counter(text.upper())
    count = 0
    for _, v in p.items():
        if v >= 2:
            count += 1
    return count


print(duplicate_count("aabbcde"))
print(duplicate_count("aabBcde"))
print(duplicate_count("indivisibility"))
print(duplicate_count(""))


def duplicate_count_v2(text: str) -> int:
    return len([x for x in set(text.lower()) if text.lower().count(x) > 1])


print(duplicate_count_v2("aabbcde"))
print(duplicate_count_v2("aabBcde"))
print(duplicate_count_v2("indivisibility"))
print(duplicate_count_v2(""))


def duplicate_count_v3(text: str) -> int:
    viewed = set()
    duplicates = set()
    for char in text:
        char = char.lower()
        if char in viewed:
            duplicates.add(char)
        viewed.add(char)
    return len(duplicates)
