#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Define TestMaxInteger class
    """

    def test_ordered(self):
        """Test ordered list of integers"""
        ordered = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer(ordered), 5)

    def test_unordered(self):
        """ test unordered list"""
        unordered = [5, 5, 7, 6, 2]
        self.assertEqual(max_integer(unordered), 7)

    def test_empty(self):
        """ test empty list"""
        empty = []
        self.assertEqual(max_integer(empty), None)


if __name__ == '__main__':
    unittest.main()
