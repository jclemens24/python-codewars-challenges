"""
Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

The keypad has the following layout:

┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘
He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4. And instead of the 5 it could also be the 2, 4, 6 or 8.

He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

* possible in sense of: the observed PIN itself and all variations considering the adjacent digits

Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list in Java/Kotlin and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results, must be strings, because of potentially leading '0's. We already prepared some test cases for you.

Detective, we are counting on you!
"""
from itertools import product


def get_pins(observed):
    adjacents = [
        "08",
        "124",
        "1235",
        "236",
        "1457",
        "24568",
        "3569",
        "478",
        "05789",
        "689",
    ]
    result = ["".join(pin) for pin in product(*(adjacents[int(d)] for d in observed))]
    return result


print(get_pins("8"))
print(get_pins("11"))

# Using dict and recursion


def get_pins_v2(observed: str) -> list:
    # These are possible numbers from the observed pin
    adjacents = {
        "1": ["2", "4"],
        "2": ["1", "5", "3"],
        "3": ["2", "6"],
        "4": ["1", "5", "7"],
        "5": ["2", "4", "6", "8"],
        "6": ["3", "5", "9"],
        "7": ["4", "8"],
        "8": ["5", "7", "9", "0"],
        "9": ["6", "8"],
        "0": ["8"],
    }

    if len(observed) == 1:
        return adjacents[observed] + [observed]
    return [
        p + d
        for p in adjacents[observed[0]] + [observed[0]]
        for d in get_pins_v2(observed[1:])
    ]


print(get_pins_v2("8"))
print(get_pins_v2("11"))


def get_pins_v3(observed: str):
    neighbors = {
        "1": ["1", "2", "4"],
        "2": ["1", "2", "3", "5"],
        "3": ["2", "3", "6"],
        "4": ["1", "4", "5", "7"],
        "5": ["2", "4", "5", "6", "8"],
        "6": ["3", "5", "6", "9"],
        "7": ["4", "7", "8"],
        "8": ["0", "5", "7", "8", "9"],
        "9": ["6", "8", "9"],
        "0": ["0", "8"],
    }

    pins = []
    for digit in observed:
        pins.append(neighbors[digit])

    for tup in product(*pins):
        yield "".join(tup)


print(get_pins_v3("8"))
for i in get_pins_v3("11"):
    print(i)
