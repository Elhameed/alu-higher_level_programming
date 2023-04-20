#!/usr/bin/python3
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
    a (int or float): The first number to be added.
    b (int or float): The second number to be added. Default is 98.

    Returns:
    int: The sum of a and b.

    Raises:
    TypeError: If either a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
