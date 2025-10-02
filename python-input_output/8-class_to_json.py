#!/usr/bin/python3
"""Module that return a dictionary description with simple data structures
(list, dictionary, string, integer and boolean) for JSON serialization of an
object.
"""


def class_to_json(obj):
    """
    Returns a dictionary description with simple data structures
    (list, dictionary, string, integer and boolean) for JSON serialization of
    an object.

    Args:
        obj (any): The object to convert to a dictionary.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__
