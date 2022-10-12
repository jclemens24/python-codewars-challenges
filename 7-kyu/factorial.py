"""
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).

More details about factorial can be found here.
"""
from math import factorial as fact


def factorial(n: int) -> int:
    if n < 0 or n > 12:
        raise ValueError
    if not n:
        return 1
    result = n
    while n > 1:
        n = n - 1
        result *= n
    return result


print(factorial(0))
print(factorial(3))
print(factorial(13))


# Using Recursion


def factorial_v2(n: int) -> int:
    if n < 0 or n > 12:
        raise ValueError
    return 1 if n <= 1 else n * factorial_v2(n - 1)


print(factorial_v2(0))
print(factorial_v2(3))
print(factorial_v2(13))

# Using Math module factorial func


def factorial_v3(n):
    if n < 0 or n > 12:
        raise ValueError
    return fact(n)


def factorial_v4(n):
    result = 1
    if n < 0 or n > 12:
        raise ValueError
    for x in range(1, n + 1):
        result *= x
    return result
