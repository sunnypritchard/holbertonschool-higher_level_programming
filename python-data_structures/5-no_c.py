#!/usr/bin/python3
'''
Function:
    no_c(my_string): removes all occurrences of 'c' and 'C' from a string

Parameters:
    my_string: input string

Returns:
    new string without 'c' and 'C'
'''


def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c != 'c' and c != 'C':
            new_string += c
    return new_string
