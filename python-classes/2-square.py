#!/usr/bin/python3
"""
This module contains a class Square that defines a square by size with
input validation.
"""


class Square:
    """A class representing a square with a validated size.

    Attributes:
        __size (int): The size of the square's side. Must be an integer >= 0.
    """

    def __init__(self, size=0):
        """Initialize a Square instance with a given size.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
