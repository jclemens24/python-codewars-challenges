"""
DESCRIPTION:
Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""
import re


def to_camel_case(text: str):
    new_text = re.split(pattern=r"_|-", string=text)
    res = ""
    for i, word in enumerate(new_text):
        if i != 0:
            res += word[:1].capitalize() + word[1:]
        else:
            res += word
    return res


print(to_camel_case("the_stealth_warrior"))
print(to_camel_case("The-Stealth-Warrior"))

# First in the regex, we create a char set looking for "_-" characters
# (.) creates a Capture Group, more specifically capture group 1, which
# is referred to in the output of our lambda func. Basically,
# this will Capitalize any character after a "-" or a "_"


def to_camel_case_v2(text: str):
    return re.sub("[_-](.)", lambda m: m.group(1).upper(), text)


print(to_camel_case_v2("the_stealth_warrior"))
print(to_camel_case_v2("The-Stealth-Warrior"))
