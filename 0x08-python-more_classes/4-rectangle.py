#!/usr/bin/python3
"""
Rectangle class
"""


class Rectangle:
    """Defines the blueprint of a rectangle"""

    def __init__(self, width=0, height=0):
        """object method"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """define width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        self._validate_non_negative_integer("width", value)
        self.__width = value

    @property
    def height(self):
        """define Height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        self._validate_non_negative_integer("height", value)
        self.__height = value

    def _validate_non_negative_integer(self, attribute, value):
        """Validate if the value is a non-negative integer"""
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")
        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")

    def area(self):
        """calculate and return the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
     """Define perimeter"""
     return (
        2 * (self.__width + self.__height)
        if self.__width and self.__height
        else 0
    )

    def __str__(self):
        """Define str"""
        return "\n".join(["#" * self.__width for _ in range(self.__height)])

    def __repr__(self):
        """Define repr"""
        return f"Rectangle({self.__width}, {self.__height})"
