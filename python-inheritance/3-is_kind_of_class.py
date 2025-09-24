#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or an instance of a class
    that inherited from a_class; otherwise False.

    param:
        obj: The object to check.
        a_class: The class to match the type of obj to.
    """
    return isinstance(obj, a_class)
