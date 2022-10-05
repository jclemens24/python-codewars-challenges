# Given an array of ints, remove the smallest value
# Do not mutate the original list


def remove_smallest(numbers: list):
    if numbers is None or len(numbers) == 0:
        return []
    copy_numbers = numbers.copy()
    copy_numbers.remove(min(numbers))
    return copy_numbers


print(remove_smallest([5, 3, 2, 1, 4]))


def remove_smallest_v2(numbers: list):
    if numbers is None or len(numbers) == 0:
        return []
    i = numbers.index(min(numbers))
    return numbers[:i] + numbers[i + 1 :]


print(remove_smallest_v2([5, 3, 2, 1, 4]))
