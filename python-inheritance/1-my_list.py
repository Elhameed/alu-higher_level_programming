#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """a subclass of list"""
    def print_sorted(self):
        """prints the sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
