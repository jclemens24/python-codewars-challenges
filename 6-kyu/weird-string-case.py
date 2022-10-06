"""
Write a function toWeirdCase (weirdcase in Ruby) that accepts a string, and returns the same string with all even indexed characters in each word upper cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the zero-ith index is even, therefore that character should be upper cased and you need to start over for each word.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there are multiple words. Words will be separated by a single space(' ').

Examples:
to_weird_case('String'); # => returns 'StRiNg'
to_weird_case('Weird string case') # => returns 'WeIrD StRiNg CaSe'
"""


def to_weird_case(words: str):
    result = ""
    for word in words.split(" "):
        result += " " + "".join(
            [
                char.title() if i % 2 == 0 else char.lower()
                for i, char in enumerate(word)
            ]
        )
    return result.strip()


print(to_weird_case("This"))


def to_weird_case_v2(words: str):
    reformat = lambda string: "".join(
        [c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(string)]
    )
    return " ".join([reformat(word) for word in words.split(" ")])


print(to_weird_case_v2("This"))
