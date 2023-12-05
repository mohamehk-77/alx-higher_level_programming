#!/usr/bin/python3
"""module"""


class Student:
    """docstring for class Student."""

    def __init__(self, first_name, last_name, age):
        """Instantiates"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary"""
        if attrs is None:
            return self.__dict__
        else:
            return {mo: hamo for mo, hamo in self.__dict__.items() if mo in attrs}
