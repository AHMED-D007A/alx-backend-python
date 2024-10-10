#!/usr/bin/env python3
"""
Module for creating a tuple from a string and a squared number.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Return a tuple where the first element is the string k,
    and the second element is the square of the int/float v as a float.
    """
    return (k, float(v ** 2))


if __name__ == "__main__":
    print(to_kv.__annotations__)
    print(to_kv("eggs", 3))
    print(to_kv("school", 0.02))
