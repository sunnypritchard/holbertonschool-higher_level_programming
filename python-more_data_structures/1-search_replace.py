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
    new_list = []
    for x in my_list:
        if x == search:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
