#!/usr/bin/python3
'''
Function:
    multiply_by_2(a_dictionary):
        Returns a new dictionary with all values multiplied by 2.
Parameters:
    a_dictionary: the dictionary to multiply.
Returns:
    A new dictionary with all values multiplied by 2.
'''


def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = a_dictionary[key] * 2
    return new_dict
