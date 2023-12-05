#!/usr/bin/python3
"""a class Square that inherits from Rectangle (9-rectangle.py)"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square is a rectangle with equal sides."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super(Square, self).__init__(size, size)
        self.__size = size
