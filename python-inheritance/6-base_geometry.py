#!/usr/bin/python3
"""
Module that defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """Calculate the area of the geometry.
        Raises:
            Exception: If the method is not implemented in a subclass.
        """
        raise Exception("area() is not implemented")
