#!/usr/bin/env python3
"""
module for gettin the string of float function.
"""


def to_str(n: float) -> str:
    """
    return the string of the given number.
    """
    return str(n)


if __name__ == "__main__":
    pi_str = to_str(3.14)
    print(pi_str == str(3.14))
    print(to_str.__annotations__)
    print("to_str(3.14) returns {} which is a {}".format(pi_str, type(pi_str)))
