#!/usr/bin/python3
"""Unittest for Square class with size attribute."""

import unittest
Square = __import__('1-square').Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_is_class(self):
        """Test if Square is a class."""
        self.assertTrue(type(Square) is type)

    def test_size_attribute(self):
        """Test if Square has size attribute after initialization."""
        sq = Square(5)
        self.assertEqual(sq._Square__size, 5)

if __name__ == '__main__':
    unittest.main()