"""
DESCRIPTION:
Define a function that takes an integer argument and returns a logical value true or false depending on if the integer is a prime.

Per Wikipedia, a prime number ( or a prime ) is a natural number greater than 1 that has no positive divisors other than 1 and itself.

Requirements
You can assume you will be given an integer input.
You can not assume that the integer will be only positive. You may be given negative numbers as well ( or 0 ).
NOTE on performance: There are no fancy optimizations required, but still the most trivial solutions might time out. Numbers go up to 2^31 ( or similar, depending on language ). Looping all the way up to n, or n/2, will be too slow.
Example
is_prime(1)  /* false */
is_prime(2)  /* true  */
is_prime(-1) /* false */
"""


from math import floor, sqrt


def is_prime(num) -> bool:
    if num <= 6:
        return num in [2, 3, 5]
    if num == 0 or num == 8 or num % 3 == 0:
        return False
    limit = floor(sqrt(num))
    for i in range(5, limit + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False

    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(-1))
print(is_prime(13))
print(is_prime(5))
print(is_prime(8))

# The above is a Brute-Force approach I use in other
# languages

# Here is more functional approach


def is_prime_v2(num: int) -> bool:
    return num > 1 and all(num % i for i in range(2, int(num**0.5 + 1)))


print(is_prime_v2(1))
print(is_prime_v2(2))
print(is_prime_v2(-1))
print(is_prime_v2(13))
print(is_prime_v2(5))
print(is_prime_v2(8))
