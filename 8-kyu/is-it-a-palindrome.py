"""
Write a function that checks if a given string (case insensitive) is a palindrome.
"""


def is_palindrome(s: str) -> bool:
    copy_s = s.lower()
    rev = reversed(copy_s)
    return copy_s == "".join(rev)


print(is_palindrome("aba"))


def is_palindrome_v2(s: str) -> bool:
    s = s.lower()
    return s == s[::-1]


print(is_palindrome_v2("aba"))
