#!/usr/bin/env python3
"""
module for concat two strings funciton.
"""


def concat(str1: str, str2: str) -> str:
    """
    return the concat of the given two strings.
    """
    return str1 + str2


if __name__ == "__main__":
    str1 = "egg"
    str2 = "shell"

    print(concat(str1, str2) == "{}{}".format(str1, str2))
    print(concat.__annotations__)
