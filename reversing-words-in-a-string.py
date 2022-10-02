"""
DESCRIPTION:
You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Example (Input --> Output)

"Hello World" --> "World Hello"
"Hi There." --> "There. Hi"
Happy coding!

"""


def reverse(st: str):
    s = st.split()[::-1]
    print(s)
    l = []
    for i in s:
        l.append(i)
    return " ".join(l)


print(reverse("Hello World"))
print(reverse("Hi There."))


def reverse_v2(st: str):
    return " ".join(reversed(st.split())).strip()


print(reverse_v2("Hello World"))
print(reverse_v2("Hi There."))
