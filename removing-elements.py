"""
DESCRIPTION:
Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

None of the arrays will be empty, so you don't have to worry about that!

"""

def remove_every_other(my_list):
  return my_list[0::2]

print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))