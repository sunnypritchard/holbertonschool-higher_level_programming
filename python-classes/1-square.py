#!/usr/bin/python3
"""This module defines a class Square with size attribute."""


class Square:
    """A class used to represent a square.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """Initialize a Square instance

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
