#!/usr/bin/python3
"""Defines a square-printing function."""


def print_square(size):
    """
    Prints a square using the "#" character.

    Args:
        size: An integer that represents the size length of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        TypeError: If size is a float and less than 0.

    Returns:
        None.

    Example:
        >>> print_square(4)
        ####
        ####
        ####
        ####
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return

    for i in range(size):
        print("#" * size)
