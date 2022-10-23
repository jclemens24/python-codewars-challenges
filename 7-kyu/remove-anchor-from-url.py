"""
DESCRIPTION:
Complete the function/method so that it returns the url with anything after the anchor (#) removed.

Examples
"www.codewars.com#about" --> "www.codewars.com"
"www.codewars.com?page=1" -->"www.codewars.com?page=1"
"""
from urllib import parse


def remove_url_anchor(url: str) -> str:
    uri = parse.urlparse(url)
    domain = url.replace(f"#{uri.fragment}", "")
    return domain


print(remove_url_anchor("www.codewars.com#about"))
print(remove_url_anchor("www.codewars.com?page=1"))
print(remove_url_anchor("www.bakedbeans.com"))


def remove_url_anchor_v2(url: str) -> str:
    return url.split("#")[0]


print(remove_url_anchor_v2("www.codewars.com#about"))
print(remove_url_anchor_v2("www.codewars.com?page=1"))
print(remove_url_anchor_v2("www.bakedbeans.com"))


def remove_url_anchor_v3(url: str) -> str:
    url_stripped = parse.urldefrag(url)
    return url_stripped[0]


print(remove_url_anchor_v3("www.codewars.com#about"))
print(remove_url_anchor_v3("www.codewars.com?page=1"))
print(remove_url_anchor_v3("www.bakedbeans.com"))


def remove_url_anchor_v4(url: str) -> str:
    index = 0
    for char in url:
        if char == "#":
            break
        index += 1
    return url[:index]


print(remove_url_anchor_v4("www.codewars.com#about"))
print(remove_url_anchor_v4("www.codewars.com?page=1"))
print(remove_url_anchor_v4("www.bakedbeans.com"))
