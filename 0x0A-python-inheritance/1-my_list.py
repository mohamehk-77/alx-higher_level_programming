#!/usr/bin/python3
"""
class MyList that inherits from list
"""


class MyList(list):

    """func prints the list, but sorted (ascending sort)"""

    def print_sorted(self):

        print(sorted(self))
