#!/usr/bin/python3
"""
This script is used to create a new user in the database. The user's information will be stored in the 'users' table of the 1-Square
"""


class Square:
    """
    Class Square

    Attributes:
    - size: size of the side of the square
    """

    def __init__(self, size):
        """
       Initializes square

       Attributes:
           size: size of a side of square
       """
        self.__size = size
