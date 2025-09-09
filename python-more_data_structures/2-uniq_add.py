#!/usr/bin/python3
'''
Function:
    uniq_add(my_list):
        Adds all unique integers in a list (only once for each integer).

Parameters:
    my_list: list of integers.

Returns:
    The sum of all unique integers.
'''


def uniq_add(my_list):
    return sum(set(my_list))
