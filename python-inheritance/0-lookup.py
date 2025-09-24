#!/usr/bin/python3
"""
This module defines a function to lookup the attributes and
methods of an object.
"""


def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    param:
        obj: The object to inspect.

    return:
        A list of strings representing the names of the attributes and methods.
    """
    return dir(obj)
