"""
DESCRIPTION:
The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

If a chunk represents an integer such as the sum of the cubes of its digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

If

sz is <= 0 or if str is empty return ""
sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
Examples:
revrot("123456987654", 6) --> "234561876549"
revrot("123456987653", 6) --> "234561356789"
revrot("66443875", 4) --> "44668753"
revrot("66443875", 8) --> "64438756"
revrot("664438769", 8) --> "67834466"
revrot("123456779", 8) --> "23456771"
revrot("", 8) --> ""
revrot("123456779", 0) --> "" 
revrot("563000655734469485", 4) --> "0365065073456944"
Example of a string rotated to the left by one position:
s = "123456" gives "234561".
"""


def fake_map(*s):
    return s


def rev_rot(strng: str, sz: int) -> str:
    if sz <= 0 or strng is None or len(strng) < sz:
        return ""
    if len(strng) == 1 and sz == 1:
        return strng
    result = ""
    for lis in map(fake_map, *([iter(strng)] * sz)):
        if not None in lis:
            result += reverse_or_rotate("".join(lis), sz)
    return result


def reverse_or_rotate(strng, sentinel):
    sums = 0

    for _, value in enumerate(strng):
        sums += pow(int(value), 2)
    if sums % 2 == 0:
        return strng[::-1]
    return strng[1:sentinel] + strng[0]


print(rev_rot("123456987654", 6))


def rev_rot_v2(strng: str, sz: int) -> str:
    if not sz or not strng:
        return ""
    strng = [
        strng[i : i + sz]
        for i in range(0, len(strng), sz)
        if len(strng[i : i + sz]) == sz
    ]
    return "".join(
        i[::-1] if sum(int(j) ** 3 for j in i) % 2 == 0 else i[1:] + i[0] for i in strng
    )


print(rev_rot_v2("123456987654", 6))
