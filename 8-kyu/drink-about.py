"""
DESCRIPTION:
Kids drink toddy.
Teens drink coke.
Young adults drink beer.
Adults drink whisky.
Make a function that receive age, and return what they drink.

Rules:

Children under 14 old.
Teens under 18 old.
Young under 21 old.
Adults have 21 or more.
Examples: (Input --> Output)

13 --> "drink toddy"
17 --> "drink coke"
18 --> "drink beer"
20 --> "drink beer"
30 --> "drink whisky"
"""


def people_with_age_drink(age: int) -> str:
    if age < 14:
        return "drink toddy"
    if age < 18:
        return "drink coke"
    if age < 21:
        return "drink beer"

    return "drink whisky"


def people_with_age_drink_v2(age: int) -> str:
    return "drink" + (
        "toddy"
        if age < 14
        else "coke"
        if age < 18
        else "beer"
        if age < 21
        else "whisky"
    )
