#!/usr/bin/python3
"""Module that defines a function that writes an object to a text file,
using a JSON representation.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    Args:
        my_obj (any): The object to write to the file.
        filename (str): The name of the file to write to.
    """
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
