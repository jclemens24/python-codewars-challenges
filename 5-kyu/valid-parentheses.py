"""
DESCRIPTION:
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters. Furthermore, the input string may be empty and/or not contain any parentheses at all. Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            try:
                stack.pop()
            except IndexError:
                return False

    if not stack:
        return True
    return False


print(valid_parentheses("()"))
print(valid_parentheses("hi(hi)()"))

# We could use a counter var to ensure we have matching num of parens


def valid_parentheses_v2(string: str):
    count = 0
    for char in string:
        if char == "(":
            count += 1
        if char == ")":
            count -= 1
        if count < 0:
            return False
    return True if count == 0 else False


print(valid_parentheses_v2("()"))
print(valid_parentheses_v2("hi(hi)()"))
