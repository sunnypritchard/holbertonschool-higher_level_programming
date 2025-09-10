#!/usr/bin/python3
"""
Function:
    best_score(a_dictionary):
        Return the key with the biggest integer value.

Parameters:
    a_dictionary: dictionary of {name: score} pairs.

Returns:
    The key (name) with the highest score, or None if the dict is empty
    or None.
"""


def best_score(a_dictionary):
    """Return the key with the largest value in the dictionary."""
    if not a_dictionary:
        return None

    max_value = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
