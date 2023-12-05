#!/usr/bin/python3
"""a model that def class BaseGeometry based on 6-base_geometry.py"""


class BaseGeometry:
    """Reprsent base geometry based on 6-base_geometry.py"""

    def area(self):
        """a function that is not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validet the value and checks for the errors.

        Args:
            name : The name of the parameter and must be str.
            value : The parameter to validate in type of int.
        Raises:
            If value is not an integer TypeError must be an integer,
            If value is not greater than 0 ValueError must be greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
