"""
DESCRIPTION:
Welcome.

In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )
"""
from string import ascii_lowercase


def alphabet_position(text: str):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in text.lower():
        if i not in alpha:
            result += ""
        else:
            pos = str(alpha.index(i) + 1) + " "
            result += pos
    return result.strip()


print(alphabet_position("The sunset sets at twelve o' clock."))


def alphabet_position_v2(text: str) -> str:
    return " ".join(str(ord(char) - 96) for char in text.lower() if char.isalpha())


print(alphabet_position_v2("The sunset sets at twelve o' clock."))


def alphabet_position_v3(text: str) -> str:
    return " ".join(
        str(ascii_lowercase.index(char.lower()) + 1) for char in text if char.isalpha()
    )


print(alphabet_position_v3("The sunset sets at twelve o' clock."))
