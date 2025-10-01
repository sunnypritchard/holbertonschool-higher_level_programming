#!/usr/bin/python3
"""Module that defines a function to read a text file (UTF8) and print it to stdout."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): The name of the file to read.
            Defaults to an empty string.
    Returns:
        str: The content of the file.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
