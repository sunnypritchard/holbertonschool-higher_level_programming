#!/usr/bin/python3
"""
Function:
    uppercase(str): Converts all lowercase letters in a string to uppercase.

Parameters:
    str (string): The input string to convert.

Returns:
    None
"""


def uppercase(str):
    for letter in str:
        if ord(letter) > 96 and ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print()
