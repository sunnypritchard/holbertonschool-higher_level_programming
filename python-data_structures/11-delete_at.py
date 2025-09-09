#!/usr/bin/python3
'''
Function:
    delete_at(my_list=[], idx=0): deletes an element at a specific position in
    a list

Parameters:
    my_list: list of integers
    idx: index of the element to delete

Returns:
    the new list with the element deleted or the original list if idx is
    invalid
'''


def delete_at(my_list=[], idx=0):
    if 0 <= idx < len(my_list):
        del my_list[idx]
    return my_list
