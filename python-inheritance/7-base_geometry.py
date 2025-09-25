#!/usr/bin/python3
"""
Module that defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """A base class for geometry-related classes."""

    """
    >>> BseGeometry.validate_integer("name", 5)
    >>> BaseGeometry.validate_integer("name", 0)
    Traceback (most recent call last):
        ...
    ValueError: name must be greater than 0
    >>> BaseGeometry.validate_integer("name", -5)
    Traceback (most recent call last):
        ...
    ValueError: name must be greater than 0
    """

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
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
