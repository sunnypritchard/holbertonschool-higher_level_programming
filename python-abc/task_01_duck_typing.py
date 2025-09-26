#!/usr/bin/python3
"""Module demonstrating duck typing in Python."""

from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Abstract method to compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method to compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle, inheriting from Shape.

    Args:
        radius (float): The radius of the circle.
    """
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Compute the area of the circle."""
        return pi * (self.radius ** 2)

    def perimeter(self):
        """Compute the perimeter (circumference) of the circle."""
        return 2 * pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle, inheriting from Shape.

    Args:
        width: The width of the rectangle.
        height: The height of the rectangle.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        """Compute the area of the rectangle."""
        return self.height * self.width

    def perimeter(self):
        """Compute the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Function that demonstrates duck typing by calling area and perimeter
    methods on any object without explicitly checking its type.

    Args:
        shape: Any object that implements area() and perimeter() methods
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Testing the duck typing functionality
if __name__ == "__main__":
    # Create instances of Circle and Rectangle
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    # Test the shape_info function with both objects
    print("Circle Information:")
    shape_info(circle)

    print("\nRectangle Information:")
    shape_info(rectangle)
