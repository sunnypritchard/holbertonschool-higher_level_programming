#!/usr/bin/python3
'''
Function:
    element_at(my_list, idx): retrieves an element from a list like in C

Parameters:
    my_list: list of elements
    idx: index of the element to retrieve

Returns:
    the element at index idx of my_list
    None if idx is negative or out of range
'''


def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
