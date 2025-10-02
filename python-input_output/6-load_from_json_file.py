#!/usr/bin/python3
"""Module that defines a function that creates an Object from a "JSON file".
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    Args:
        filename (str): The name of the JSON file to load.

    Returns:
        any: The object represented by the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
