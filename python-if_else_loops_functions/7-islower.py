#!/usr/bin/python3
"""
Functions:
    islower(c): Checks if a given character is a lowercase letter.

Parameters:
    c (str): A single character to check.

Returns:
    bool: True if the character is lowercase, False otherwise.
"""


def islower(c):
    if ord(c) < 97:
        return False
    return True
