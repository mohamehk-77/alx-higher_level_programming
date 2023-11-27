#!/usr/bin/python3
"""
Represents a rectangle with width and height

"""


class Rectangle:
    """Represents a rectangle with width and height."""

    def __init__(self, width=0, height=0):
        """
        Initializes a new Rectangle.

        :param width: The width of the rectangle (default is 0).
        :param height: The height of the rectangle (default is 0).
        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        :param value: The new width value.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
        if not isinstance(value, int):
            raise ValueError("Width must be an integer")
        if value < 0:
            raise ValueError("Width must be >= 0")
        self._width = value

        @property
        def height(self):
            """Get the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            """
        Set the height of the rectangle.

        :param value: The new height value.
        :raises TypeError: If the value is not an integer.
        :raises ValueError: If the value is less than 0.
        """
            if not isinstance(value, int):
                raise ValueError("Height must be an integer")
            if value < 0:
                raise ValueError("Height must be >= 0")
            self._height = value
