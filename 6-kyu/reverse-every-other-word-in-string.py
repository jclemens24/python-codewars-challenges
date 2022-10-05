"""
DESCRIPTION:
Reverse every other word in a given string, then return the string. Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. Punctuation marks should be treated as if they are a part of the word in this kata.
"""


def reverse_alternate(string: str):
    l = string.split()
    print(l)
    for i in range(1, len(l), 2):
        l[i] = l[i][::-1].strip()
    return " ".join(l)


print(reverse_alternate("Did it work?"))
print(reverse_alternate("I really hope it works this time..."))
print(reverse_alternate("This       is a test"))


def reverse_alternate_v2(string: str):
    words = string.split()
    words[1::2] = [word[::-1] for word in words[1::2]]
    return " ".join(words)


print(reverse_alternate_v2("Did it work?"))
print(reverse_alternate_v2("I really hope it works this time..."))
print(reverse_alternate_v2("This       is a test"))
