#!/usr/bin/python3
"""
Module that defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """A class representing base geometry."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a value is a positive integer.

        Args:
            name (str): The name of the variable being validated.
            value (int): The value to validate.
        Raises:
            TypeError: must be an integer.
            ValueError: must be greater than 0.
        """
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
