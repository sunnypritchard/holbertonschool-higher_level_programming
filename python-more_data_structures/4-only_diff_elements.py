#!/usr/bin/python3
'''
Function:
    only_diff_elements(set_1, set_2):
        Returns a set of elements present in only one of the two sets.

Parameters:
    set_1: first set.
    set_2: second set.

Returns:
    A set of elements present in only one of the two sets.
'''


def only_diff_elements(set_1, set_2):
    return set_1 ^ set_2
