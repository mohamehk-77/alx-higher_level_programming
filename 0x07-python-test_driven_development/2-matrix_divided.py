#!/usr/bin/python3
"""
    A function that divides all elements of a matrix.
Args:
        matrix:  (list of lists): The matrix of integers or floats.
        div:  (int or float): The divisor.
        
Returns:
        new matrix
Raises:
        TypeError: If matrix is not a list of lists of integers or floats,
                   if each row of the matrix doesn't have the same size,
                   or if div is not a number.
        ZeroDivisionError: If div is equal to 0.

"""


def matrix_divided(matrix, div):
    """
    def matrix_divided(matrix, div)
    Module for matrix division

    """
    if not all(isinstance(row, list) for row in matrix) or not all(
            isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(num / div, 2) for num in row] for row in matrix]
