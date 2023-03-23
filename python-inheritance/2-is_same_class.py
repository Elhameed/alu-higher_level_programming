#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """Returns True if obj is an instance of a_class; otherwise False."""
    return type(obj) is a_class
