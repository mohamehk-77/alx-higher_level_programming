#!/usr/bin/python3
"""Unit test for Rectangle class."""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class RectangleTestCase(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Reset the id counter before each test."""
        Base._Base__nb_objects = 0

    def test_rectangle_id_increment(self):
        """Test that the id is incremented correctly."""
        r1 = Rectangle(4, 5)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 3, 0, 0)
        self.assertEqual(r2.id, 2)

    def test_rectangle_attributes(self):
        """Test that Rectangle instances have the correct attributes."""
        r = Rectangle(3, 4, 1, 2, 10)
        self.assertEqual(r.width, 3)
        self.assertEqual(r.height, 4)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 10)

    def test_rectangle_area(self):
        """Test the area method of the Rectangle class."""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_rectangle_str_representation(self):
        """Test the __str__ method of the Rectangle class."""
        r = Rectangle(2, 3, 4, 5, 6)
        self.assertEqual(str(r), "[Rectangle] (6) 4/5 - 2/3")

    def test_rectangle_update(self):
        """Test the update method of the Rectangle class."""
        r = Rectangle(2, 3, 4, 5, 6)
        r.update(10, 5, 6, 7, 8)
        self.assertEqual(str(r), "[Rectangle] (10) 7/8 - 5/6")

    # Add more test cases as needed


if __name__ == '__main__':
    unittest.main()
