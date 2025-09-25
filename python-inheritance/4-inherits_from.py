#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of a
specified class, excluding instances of the class itself.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class or aninheritance
    inheritance of a_class; otherwise False.

    param:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
