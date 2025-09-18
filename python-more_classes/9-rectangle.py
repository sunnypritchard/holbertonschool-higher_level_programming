#!/usr/bin/python3

"""Defines a Rectangle class."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle. Default is 0.
            height (int): The height of the rectangle. Default is 0.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    @classmethod
    def square(cls, size=0):
        """Creates a new Rectangle instance with width and height equal to
        size.

        Args:
            size (int): The size of the square's sides. Default is 0.

        Returns:
            Rectangle: A new Rectangle instance with width and height equal
            to size.
        """
        return cls(size, size)

    @property
    def width(self):
        """Retrieves the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If width is not an integer.
            ValueError: If width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If height is not an integer.
            ValueError: If height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Returns a string representation of the rectangle using print_symbol.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += symbol * self.__width
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """
        Returns a string representation of the rectangle that can be used to
        recreate it.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Prints a message when a Rectangle instance is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the one with the larger area.

        Args:
            rect_1 (Rectangle): The first rectangle to compare.
            rect_2 (Rectangle): The second rectangle to compare.

        Returns:
            Rectangle: The rectangle with the larger area. If both have the
            same area, returns rect_1.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of
            Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
