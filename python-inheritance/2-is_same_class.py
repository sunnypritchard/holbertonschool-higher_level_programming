#! /usr/bin/env python3
"""
Module that defines a function to check if an object is exactly an instance
of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class.
    Otherwise False.

    param:
        obj: The object to check.
        a_class: The class to match the type of obj to.

    """
    return type(obj) is a_class


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))