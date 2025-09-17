#!/usr/bin/python3
"""Unittest for Square class with private size attribute."""

import unittest
Square = __import__('1-square').Square


class TestSquare(unittest.TestCase):
    def test_type(self):
            """Test if Square is a class."""
            self.assertTrue(type(Square) is type)

    def test_size_attribute(self):
        """Test if Square has a private size attribute."""
        sq = Square(5)
        self.assertTrue(hasattr(sq, '_Square__size'))
        self.assertFalse(hasattr(sq, 'size'))
        self.assertFalse(hasattr(sq, '__size'))
        self.assertEqual(sq._Square__size, 5)

if __name__ == '__main__':
    unittest.main()