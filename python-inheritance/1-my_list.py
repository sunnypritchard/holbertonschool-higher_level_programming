#!/usr/bin/python3
"""
This module defines a MyList class that inherits from list
and includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    MyList class that inherits from list
    """
    def print_sorted(self):
        """
        Prints the list in ascending order
        """
        print(sorted(self))
