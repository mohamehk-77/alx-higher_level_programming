#!/usr/bin/python3

"""
Check if the object is an instance of a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is exactly an instance of a_class.
    """
    return isinstance(obj, a_class)
