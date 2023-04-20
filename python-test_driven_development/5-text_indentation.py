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
    if type(text) is not str:
        raise TypeError("text must be a string")

    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print("{}".format(text), end="")
