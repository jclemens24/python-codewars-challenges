"""
DESCRIPTION:
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
"""

import ipaddress


def is_valid_IP(strng: str):
    """
    I was actually proud of this solution. Apparently, many others also thought of this"""
    try:
        addr = ipaddress.ip_address(strng)
        if addr:
            return True
    except ValueError:
        return False


print(is_valid_IP("12.255.56.1"))
print(is_valid_IP(""))
print(is_valid_IP("abc.def.ghi.jkl"))


def is_valid_IP_v2(strng: str):
    addr = strng.split(".")
    return all(x in map(str, range(256)) for x in addr) and len(addr) == 4
