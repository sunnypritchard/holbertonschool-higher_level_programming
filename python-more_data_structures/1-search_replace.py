#!/usr/bin/python3
'''
Function:
    search_replace(my_list, search, replace):
        Replaces all occurrences of an element by another in a new list.

Parameters:
    my_list: list of elements.
    search: element to replace in the list.
    replace: new element.

Returns:
    A new list.
'''


def search_replace(my_list, search, replace):
    return [replace if x == search else x for x in my_list]
