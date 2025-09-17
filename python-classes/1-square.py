#!/usr/bin/python3
"""
This module defines the Square class for representing squares by their size.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """Initializes a Square instance.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
