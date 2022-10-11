"""
DESCRIPTION:
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
The code would be called like so:

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
"""
from itertools import takewhile
from string import whitespace
from re import MULTILINE, escape, sub


def strip_comments(strng: str, markers: list):
    filter_text = strng.split("\n")
    for marker in markers:
        filter_text = [s.split(marker)[0].rstrip() for s in filter_text]
    return "\n".join(filter_text)


print(
    strip_comments(" apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
)


def strip_comments_v2(strng, markers: list):
    def inner():
        for line in strng.split("\n"):
            yield "".join(takewhile(lambda char: char not in markers, line)).rstrip(
                whitespace
            )

    return "\n".join(inner())


print(
    strip_comments_v2(
        " apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
    )
)


def strip_comments_v3(strng: str, markers: list) -> str:
    strng_to_list = strng.split("\n")
    res = []
    for line in strng_to_list:
        for marker in markers:
            if marker in line:
                line = line[: line.find(marker)].rstrip()
        res.append(line)
    return "\n".join(res)


print(
    strip_comments_v3(
        " apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
    )
)


def strip_comments_v4(strng: str, markers: list):
    return (
        strng
        if not markers
        else sub(f" *[{escape(''.join(markers))}].*", "", strng, MULTILINE)
    )


print(
    strip_comments_v4(
        " apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]
    )
)
