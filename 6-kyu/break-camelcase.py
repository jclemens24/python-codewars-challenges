"""
Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""
"""
from re import sub


def solution(s: str) -> str:
    return "".join([" " + char if char.isupper() else char for char in s])


print(solution("camelCasing"))


def solution_v2(s: str) -> str:
    return sub("([A-Z])", r" \1", s)


print(solution_v2("camelCasing"))
