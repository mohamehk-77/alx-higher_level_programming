#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[0 for _ in o] for o in matrix]
    for i in range(len(matrix)):
        for y in range(len(matrix[i])):
            new_matrix[i][y] = matrix[i][y] ** 2
    return new_matrix
           