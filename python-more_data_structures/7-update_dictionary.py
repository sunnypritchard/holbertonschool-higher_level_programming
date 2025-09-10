#!/usr/bin/python3
"""Replaces or adds key/value in a dictionary.

Args:
    a_dictionary (dict): The dictionary to update.
    key: The key to replace or add.
    value: The value associated with the key.

Returns:
    dict: The updated dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
