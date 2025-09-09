#!/usr/bin/python3
'''
Function:
    square_matrix_simple(matrix=[]):
        Computes the square value of all integers of a matrix.

Parameters:
    matrix: list of lists of integers.

Returns:
    A new matrix representing the square value of all integers of the input matrix.
'''


def square_matrix_simple(matrix=[]):
    return [[x**2 for x in row] for row in matrix]
