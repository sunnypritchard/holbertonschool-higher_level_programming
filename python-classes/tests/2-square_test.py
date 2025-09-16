#!/usr/bin/python3
"""Unittest for Square class."""

import unittest
Square = __import__('2-square').Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_is_class(self):
        """Test if Square is a class."""
        self.assertTrue(type(Square) is type)

    def test_size_attribute(self):
        """Test if Square has size attribute after initialization."""
        sq = Square(5)
        self.assertEqual(sq._Square__size, 5)

    def test__size_not_integer(self):
        """Test TypeError is raised if size is not an integer."""
        with self.assertRaises(TypeError) as cm:
            Square("4")
        self.assertEqual(str(cm.exception), "size must be an integer")

        with self.assertRaises(TypeError) as cm:
            Square(3.5)

    def test_valid_size_default(self):
        """Test if Square initializes size to 0 by default."""
        sq = Square()
        self.assertEqual(sq._Square__size, 0)

    def test_size_negative(self):
        """Test ValueError is raised if size is negative."""
        with self.assertRaises(ValueError) as cm:
            Square(-3)
        self.assertEqual(str(cm.exception), "size must be >= 0")


if __name__ == '__main__':
    unittest.main()