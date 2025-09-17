#!/usr/bin/python3

import unittest
Square = __import__('4-square').Square


class TestSquare(unittest.TestCase):

    def test_area_and_size(self):
        """
        Test that the area method returns the correct area and that size
        property works as expected.
        """
        sq = Square(89)
        self.assertEqual(sq.area(), 7921)
        self.assertEqual(sq.size, 89)

        sq.size = 3
        self.assertEqual(sq.area(), 9)
        self.assertEqual(sq.size, 3)

    def test_invalid_size_assignment(self):
        """
        Test that assigning an invalid value to the size property raises
        the appropriate exception.
        """
        sq = Square(1)
        with self.assertRaises(TypeError) as cm:
            sq.size = "5 feet"
        self.assertEqual(str(cm.exception), "size must be an integer")


if __name__ == "__main__":
    unittest.main()
