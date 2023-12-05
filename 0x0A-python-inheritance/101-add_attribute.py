#!/usr/bin/python3
"""module"""


def add_attribute(obj, per, value):
    """Adds an attribute to the given object with a specific permission and value."""

    if not hasattr(obj, "__dict__"):

        raise TypeError("can't add new attribute")

    setattr(obj, per, value)
