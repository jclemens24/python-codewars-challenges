"""
DESCRIPTION:
Our football team finished the championship. The result of each match look like "x:y". Results of all matches are recorded in the collection.

For example: ["3:1", "2:2", "0:1", ...]

Write a function that takes such collection and counts the points of our team in the championship. Rules for counting points for each match:

if x > y: 3 points
if x < y: 0 point
if x = y: 1 point
Notes:

there are 10 matches in the championship
0 <= x <= 4
0 <= y <= 4
"""


def points(games: list):
    total_points = 0

    for game in games:
        match = game.split(":")
        if match[0] > match[1]:
            total_points += 3
        if match[0] == match[1]:
            total_points += 1
    return total_points


print(points(["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"]))


def points_v2(games: list[str]):
    return sum([0, 1, 3][1 + (g[0] > g[2]) - (g[0] < g[2])] for g in games)


print(points_v2(["1:0", "2:0", "3:0", "4:0", "2:1", "3:1", "4:1", "3:2", "4:2", "4:3"]))
