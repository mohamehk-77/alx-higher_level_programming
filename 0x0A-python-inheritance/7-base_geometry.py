#!/usr/bin/python3
"""
class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry:

    """class"""

    def area(self):
        """Area"""

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validator"""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
