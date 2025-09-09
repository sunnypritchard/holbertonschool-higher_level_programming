#!/usr/bin/python3
'''
Function:
    print_sorted_dictionary(a_dictionary):
        Prints a dictionary by ordered keys.

Parameters:
    a_dictionary: the dictionary to print.

Returns:
    None
'''


def print_sorted_dictionary(a_dictionary):
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]), end="\n")
