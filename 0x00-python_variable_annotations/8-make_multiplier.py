#!/usr/bin/env python3
"""
Module for creating a multiplier function.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Return a function that multiplies a float by the given multiplier.
    """
    def multiplier_function(value: float) -> float:
        return value * multiplier

    return multiplier_function


if __name__ == "__main__":
    print(make_multiplier.__annotations__)
    fun = make_multiplier(2.22)
    print("{}".format(fun(2.22)))
