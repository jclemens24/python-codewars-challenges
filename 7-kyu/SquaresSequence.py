"""
Complete the function that returns an array of length n, starting with the given number x and the squares of the previous number. If n is negative or zero, return an empty array/list.

Examples
2, 5  -->  [2, 4, 16, 256, 65536]
3, 3  -->  [3, 9, 81]
"""

from itertools import accumulate, repeat

def squares(x: int, n: int) -> list[int]:
  if not n or n <= 0: return []
  result = []
  i = 0
  while (i < n):
    if i == 0:
      result.append(x)
      i += 1
    else:
      squared = x ** 2
      result.append(squared)
      x = squared
      i += 1
  return result

print(squares(2, 5))
print(squares(10, 4))

def squares_v2(x: int, n: int) -> list[int]:
  return [x ** (2 ** i) for i in range(0, n)]

print(squares_v2(2, 5))
print(squares_v2(10, 4))

def squares_v3(x: int, n: int) -> list[int]:
  return list(accumulate(repeat(x, n), lambda a, _: a * a))

print(squares_v3(2, 5))
print(squares_v3(10, 4))