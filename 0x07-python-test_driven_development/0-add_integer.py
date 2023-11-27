#!/usr/bin/python3

"""
func that add integer
Args:
        a (int or float): The first number.
        b (int or float): The second number. Defaults to 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.

"""


def add_integer(a, b=98):
    """
    add 2 integer

    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    try:
        a = int(a)
    except ValueError:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except ValueError:
        raise TypeError("b must be an integer")
    return a + b
