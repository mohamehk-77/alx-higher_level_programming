#!/usr/bin/python3
"""
    Prints a formatted string with the given first and last names.

    Args:
        first_name (str): The first name.
        last_name (str): The last name. Defaults to an empty string.

    Raises:
        TypeError: If first_name or last_name is not a string.
"""


def say_my_name(first_name, last_name=""):
    """func that call my name"""

    if not isinstance(first_name, str):
        raise TypeError("First name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("Last name must be a string")

    if last_name:
        print(f"My full name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name}")
