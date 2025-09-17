#!/usr/bin/python3
"""Unittest for Square class."""

import unittest
Square = __import__('2-square').Square


class TestSquare(unittest.TestCase):
    def test_default_size(self):
        """Test if Square initializes with default size 0."""
        sq = Square()
        self.assertEqual(sq._Square__size, 0)

    def test_type_error(self):
        """Test that non-integer size raises TypeError."""
        with self.assertRaises(TypeError) as cm:
            Square("a")
        self.assertEqual(str(cm.exception), "size must be an integer")
        with self.assertRaises(TypeError) as cm:
            Square(3.14)
        self.assertEqual(str(cm.exception), "size must be an integer")

    def test_value_error(self):
        """Test that negative size raises ValueError."""
        with self.assertRaises(ValueError) as cm:
            Square(-1)
        self.assertEqual(str(cm.exception), "size must be >= 0")


if __name__ == '__main__':
    unittest.main()