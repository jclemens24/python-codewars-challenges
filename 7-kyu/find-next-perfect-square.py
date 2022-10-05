from math import sqrt


def find_next_square(sq):
    if int(sq**0.5) != sq**0.5:
        return -1
    base = sqrt(sq)
    return pow(base + 1, 2)


print(find_next_square(121))
print(find_next_square(625))
print(find_next_square(114))


def find_next_square_v2(sq: int):
    base = sq**0.5
    if base.is_integer():
        return (base + 1) ** 2
    return -1


print(find_next_square_v2(121))
print(find_next_square_v2(625))
print(find_next_square_v2(114))


def find_next_square_v3(sq: int) -> int:
    base = sq**0.5
    return -1 if base % 1 else (base + 1) ** 2
