#!/usr/bin/python3
'''
Function:
    Raises a TypeError exception.

Parameters:
    None

Returns:
    None
'''


def raise_exception():
    raise TypeError("This is a type error")


if __name__ == "__main__":
    try:
        raise_exception()
    except TypeError as te:
        print("Exception raised")
