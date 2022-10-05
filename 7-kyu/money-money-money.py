from math import log, ceil


def calculate_years(principal, interest, tax, desired):
    total = principal
    years = 0

    while total < desired:
        earned = total * interest
        earned = earned - (earned * tax)
        total += earned
        years += 1

    return years


print(calculate_years(1000, 0.05, 0.18, 1100))


def calculate_years_v2(principal, interest, tax, desired):
    if principal >= desired:
        return 0

    return ceil(log(float(desired) / principal, 1 + interest * (1 - tax)))


print(calculate_years_v2(1000, 0.05, 0.18, 1100))
