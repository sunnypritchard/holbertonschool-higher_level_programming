import unittest
from io import StringIO
import sys


Square = __import__('5-square').Square


class TestSquarePrint(unittest.TestCase):
    def test_my_print(self):
        sq = Square(3)
        expected_3 = "###\n###\n###\n"
        captured = StringIO()
        sys.stdout = captured
        sq.my_print()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected_3)

        sq.size = 10
        expected_10 = ("#" * 10 + "\n") * 10
        captured = StringIO()
        sys.stdout = captured
        sq.my_print()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), expected_10)

        sq.size = 0
        captured = StringIO()
        sys.stdout = captured
        sq.my_print()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n")


if __name__ == "__main__":
    unittest.main()
