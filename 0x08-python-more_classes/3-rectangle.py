#!/usr/bin/python3
class Rectangle:
    """Class to represent a rectangle."""

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter func for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter func for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter func for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter func for height."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Define perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Define"""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
        for i in range(self.__height):
            result += "#" * self.__width
            if i < self.__height - 1:
                result += "\n"
        return result
