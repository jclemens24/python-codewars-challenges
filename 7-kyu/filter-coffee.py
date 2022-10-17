"""
You love coffee and want to know what beans you can afford to buy it.

The first argument to your search function will be a number which represents your budget.

The second argument will be an array of coffee bean prices.

Your 'search' function should return the stores that sell coffee within your budget.

The search function should return a string of prices for the coffees beans you can afford. The prices in this string are to be sorted in ascending order.
"""


def search(budget: int, prices: list[int]):
    result = []
    for price in sorted(prices):
        if price <= budget:
            result.append(str(price))
    return ",".join(result)


print(search(3, [6, 1, 2, 9, 2]))
print(search(10, [0, 0, 0]))
print(search(10, []))
