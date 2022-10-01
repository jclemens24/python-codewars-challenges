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

# An easier solution would have been to just define 'step'

def remove_every_other_v2(my_list):
  return my_list[::2]

print(remove_every_other_v2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# More programmtic is to build a new list
# This gives better type inference if desired

def remove_other_other_v3(my_list):
  result = []

  for i in range(len(my_list)):
    if i % 2 == 0:
      result.append(my_list[i])
  return result