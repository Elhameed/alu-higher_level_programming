#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """
    Prints the given text with 2 new lines after each given occurence.

    Args:
        text (str): The input text to be indented.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ('.', '?', ':'):
            print("\n\n", end="")
