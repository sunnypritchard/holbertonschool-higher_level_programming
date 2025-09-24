#!/usr/bin/python3
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
