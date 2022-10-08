"""
DESCRIPTION:
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
"""
alpha = "abcdefghijklmnopqrstuvwxyz"


def high(x: str) -> str:
    top_word = ""
    high_score = 0
    temp_score = 0
    words = x.split()
    for word in words:
        for char in word:
            temp_score += alpha.index(char) + 1
        if temp_score > high_score:
            high_score = temp_score
            top_word = word
        temp_score = 0
    return top_word


print(high("man i need a taxi up to ubud"))
print(high("what time are we climbing up the volcano"))


def high_v2(x: str) -> str:
    return max(x.split(), key=lambda word: sum(ord(char) - 96 for char in word))


print(high_v2("man i need a taxi up to ubud"))
print(high_v2("what time are we climbing up the volcano"))


def high_v3(x: str) -> str:
    words = x.split()
    nums = []
    for word in words:
        scores = [sum(ord(char) - 96 for char in word)]
        nums.append(scores)
    print(nums)
    return words[nums.index(max(nums))]


print(high_v3("man i need a taxi up to ubud"))
print(high_v3("what time are we climbing up the volcano"))
