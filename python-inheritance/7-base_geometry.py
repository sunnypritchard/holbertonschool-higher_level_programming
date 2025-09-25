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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
