#!/usr/bin/python3

import unittest
Square = __import__('3-square').Square

class TestSquare(unittest.TestCase):
    def test_area(self):
        """
        Test that the area method returns the correct area for squares of different sizes.
        """
        sq1 = Square(3)
        self.assertEqual(sq1.area(), 9)
        sq2 = Square(5)
        self.assertEqual(sq2.area(), 25)


if __name__ == '__main__':
    unittest.main()