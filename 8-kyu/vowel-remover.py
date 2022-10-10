"""
DESCRIPTION:
Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.

Examples
"hello"     -->  "hll"
"codewars"  -->  "cdwrs"
"goodbye"   -->  "gdby"
"HELLO"     -->  "HELLO"
don't worry about uppercase vowels
y is not considered a vowel for this kata
"""
import re


def shortcut(s: str) -> str:
    return re.sub(r"[aeiou]", "", string=s)


print(shortcut("hellO"))
print(shortcut("codewars"))
print(shortcut("HELLO"))
print(shortcut("goodbye"))


def shortcut_v2(s: str) -> str:
    for vowel in "aeiou":
        s = s.replace(vowel, "")
    return s


print(shortcut_v2("hellO"))
print(shortcut_v2("codewars"))
print(shortcut_v2("HELLO"))
print(shortcut_v2("goodbye"))


def shortcut_v3(s: str) -> str:
    return "".join([char for char in s if char not in "aeiou"])


print(shortcut_v3("hellO"))
print(shortcut_v3("codewars"))
print(shortcut_v3("HELLO"))
print(shortcut_v3("goodbye"))
