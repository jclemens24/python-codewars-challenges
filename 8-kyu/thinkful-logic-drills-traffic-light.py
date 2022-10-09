"""
You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow.
"""


def update_light(current: str):
    next_light = {"red": "green", "green": "yellow", "yellow": "red"}

    return next_light.get(current)


print(update_light("green"))
print(update_light("yellow"))

update_light_v2 = lambda curr, lights=["yellow", "green", "red"]: lights[
    lights.index(curr) - 1
]

print(update_light_v2("red"))
