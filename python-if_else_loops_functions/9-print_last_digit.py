#!/usr/bin/python3
"""
Function:
    print_last_digit(number): Prints the last digit of a number.

Parameters:
    number (int): The input number.

Returns:
    int: The last digit of the number.
"""


def print_last_digit(number):

    last_digit = number % 10 if number >= 0 else (abs(number) % 10)
    print("{}".format(last_digit), end="")
    return last_digit
