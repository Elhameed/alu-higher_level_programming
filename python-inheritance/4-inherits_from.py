#!/usr/bin/python3
"""checks if object is an instance of a class
that inherited
"""


def inherits_from(obj, a_class):
    """returns true if object is an instance of a class
    or a class that inherited from the specifed class
    """
    return (issubclass(obj, a_class))
