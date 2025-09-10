#!/usr/bin/python3
'''
Function:
    simple_delete(a_dictionary, key=""):
        Deletes a key in a dictionary.

Parameters:
    a_dictionary: the dictionary to modify.
    key: the key to delete.

Returns:
    The modified dictionary.
'''


def simple_delete(a_dictionary, key=""):
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
