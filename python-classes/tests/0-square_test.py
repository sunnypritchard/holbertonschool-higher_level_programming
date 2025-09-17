#!/usr/bin/python3
"""Unittest for Square class."""

import unittest
Square = __import__('0-square').Square


class TestSquare(unittest.TestCase):
	def test_type(self):
		"""Test if Square is a class."""
		self.assertTrue(type(Square) is type)

	def test_no_attributes(self):
		"""Test if Square has no attributes by default."""
		self.assertEqual(Square().__dict__, {})

if __name__ == '__main__':
	unittest.main()
