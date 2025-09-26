#!/usr/bin/python3
"""Module demonstrating duck typing in Python."""
import math
from abc import ABC, abstractmethod


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
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
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
