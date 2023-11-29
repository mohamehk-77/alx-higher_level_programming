#!/usr/bin/python3
"""
Represents a rectangle with width and height

"""


class Rectangle:
    """A class to represent a rectangle."""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width cannot be >= 0")
        self.width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height cannot be >= 0")
        self.height = value
