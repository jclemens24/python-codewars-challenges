from collections import Counter

""" Returns first non repeating char in a string"""

def first_non_repeating_character(string: str):
    upper = string.upper()
    index = 0
    for char in upper:
        if upper.index(char) == upper.rindex(char):
            index = upper.index(char)
            return string[index]
    return ''


print(first_non_repeating_character('a'))
print(first_non_repeating_character("stress"))
print(first_non_repeating_character('abba'))


def first_non_repeating_letter(string: str):
    lower = string.lower()
    for i, char in enumerate(lower):
        if lower.count(char) == 1:
            return string[i]
    return ''


print(first_non_repeating_letter('a'))
print(first_non_repeating_letter("stress"))
print(first_non_repeating_letter('abba'))


def first_non_repeating_letter_v2(string: str):
    count = Counter(string.lower())
    print(count.items())
    for letter in string:
        if count[letter.lower()] == 1:
            return letter
    return ''


print(first_non_repeating_letter_v2("stress"))

# Using List Comprehension


def first_non_repeating_letter_v3(string: str):
    unique = [
        char for char in string if string.lower().count(
            char.lower()) == 1]
    return unique[0] if unique else ''


print(first_non_repeating_letter_v3('a'))
print(first_non_repeating_letter_v3("stress"))
print(first_non_repeating_letter_v3('abba'))
