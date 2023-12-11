#!/usr/bin/python3
"""Unit test for Square class."""
import unittest
from models.square import Square
from models.base import Base


class SquareTestCase(unittest.TestCase):
    """Test cases for the Square class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def test_square_id_increment(self):
        """Test that the id is incremented correctly."""
        s1 = Square(5)
        self.assertEqual(s1.id, 1)

        s2 = Square(2, 0, 0)
        self.assertEqual(s2.id, 2)

    def test_square_attributes(self):
        """Test that Square instances have the correct attributes."""
        s = Square(3, 1, 2, 10)
        self.assertEqual(s.size, 3)
        self.assertEqual(s.x, 1)
        self.assertEqual(s.y, 2)
        self.assertEqual(s.id, 10)

    def test_square_area(self):
        """Test the area method of the Square class."""
        s = Square(4)
        self.assertEqual(s.area(), 16)

    def test_square_str_representation(self):
        """Test the __str__ method of the Square class."""
        s = Square(2, 3, 4, 5)
        self.assertEqual(str(s), "[Square] (5) 3/4 - 2")

    def test_square_update(self):
        """Test the update method of the Square class."""
        s = Square(2, 3, 4, 5)
        s.update(10, 5, 6, 7)
        self.assertEqual(str(s), "[Square] (10) 6/7 - 5")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
