#!/usr/bin/python3
"""This module defines a class Square with private size attribute."""


class Square:
    """A class Square that defines a square with a private size attribute.

    Attributes:
        __size (int): The size of the square's side.
    """

    def __init__(self, size):
        """Initialize a Square instance with a private size attribute.

        Args:
            size (int): The size of the square's side.
        """
        self.__size = size
