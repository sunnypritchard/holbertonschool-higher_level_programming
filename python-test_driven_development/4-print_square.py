#!/usr/bin/env python3
"""
This is the "print_square" module

This module supplies one function: print_square(). For example,

>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    This function prints a square with '#' character to represent it.
        'size' must but an integer.
        'size' is used to define the width and height of the square.
    A TypeError is raised if size is not an integer.
    A ValueError is raised if size is negative.
    """
    if not isinstance(size, int):
        if isinstance(size, float) and size < 0:
            raise TypeError("size must be an integer")
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
