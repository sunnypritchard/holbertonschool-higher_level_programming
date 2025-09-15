#!/usr/bin/python3
'''
This module provides a function to divide a matrix by a divisor.
'''


def matrix_divided(matrix, div):
    '''
    Divides all elements of a matrix by a divisor.

    Parameters:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The divisor.

    Returns:
        list of lists: A new matrix with each element divided by div and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats,
                   if rows of the matrix are not of the same size,
                   or if div is not a number (int or float).
    '''
    if not isinstance(matrix, list):
        raise TypeError(
            (
                "matrix must be a matrix (list of lists) of "
                "integers/floats"
            )
        )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if not all(
        isinstance(elem, (int, float))
        for row in matrix
        for elem in row
    ):
        raise TypeError(
            (
                "matrix must be a matrix (list of lists) "
                "of integers/floats"
            )
        )
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must be of the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(elem / div, 2) for elem in row] for row in matrix]
