#!/usr/bin/python3
"""
This module defines the Square class for representing squares by their size.
"""


class Square:
    """A class that defines a square by its size.

    Attributes:
        size (int): The size of the square's side. Must be an integer >= 0.
    """

    def __init__(self, size=0):
        """Initializes a Square instance.

        Args:
            size (int, optional): The size of the square's side. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Will call the property setter for validation

    @property
    def size(self):
        """Getter for the size of the square.

        Returns:
            int: The size of the square's side.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for the size of the square with validation.

        Args:
            value (int): The new size of the square's side.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.size ** 2
