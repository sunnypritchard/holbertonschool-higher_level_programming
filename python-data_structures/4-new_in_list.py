#!/usr/bin/python3
'''
Function:
    new_in_list(my_list, idx, element): replaces an element in a copy of a list
    at a specific index

Parameters:
    my_list: list of integers
    idx: index of the element to replace
    element: new element to insert

Returns:
    new list with the updated element
'''


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
