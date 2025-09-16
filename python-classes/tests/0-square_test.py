#!/usr/bin/python3
"""Unittest for Square class."""


import unittest
Square = __import__("0-square").Square


class TestSquare(unittest.TestCase):
    """Test cases for Square class."""

    def test_square_is_class(self):
        """Test if Square is a class."""
        self.assertTrue(type(Square) is type)

    def test_no_attributes(self):
        """Test if Square has no attributes by default."""
        sq = Square()
        self.assertEqual(sq.__dict__, {})

if __name__ == '__main__':
    unittest.main()
