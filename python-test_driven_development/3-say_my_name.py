#!/usr/bin/python3
"""
This is the "say_my_name" module.

The say_my_name module supplies one function, say_my_name().  For example,

>>> say_my_name("John", "Doe")
My name is John Doe
"""


def say_my_name(first_name, last_name=""):
    """
    This function prints "My name is <first_name> <last_name>"
    It need a first name as input but can omit the last name
    Both arguments needs to be a string
    Raises a TypeError if either arguments are not strings.
    """
    if not isinstance(first_name, str):
        raise TypeError("name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("name must be a string")
    print("My name is {} {}".format(first_name, last_name))
