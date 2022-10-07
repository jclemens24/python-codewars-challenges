"""
DESCRIPTION:
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""


def abbrev_name(name: str):
    first, last = name.split(" ")
    return first[0:1].upper() + "." + last[0:1].upper()


print(abbrev_name("Sam Harris"))


def abbrev_names_v2(name: str):
    names = name.split()
    return f"{names[0][0]}.{names[1][0]}".upper()


print(abbrev_names_v2("Sam Harris"))


def abbrev_name_v3(name: str) -> str:
    return ".".join(char[0].upper() for char in name.split())


print(abbrev_name_v3("Sam Harris"))
