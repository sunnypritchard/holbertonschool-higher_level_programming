#!/usr/bin/python3
'''
Function:
    multiply_list_map(my_list=[], number=0):
        Returns a list with all values multiplied by a number using map.
Parameters:
    my_list: list of integers.
    number: number to multiply by.
Returns:
    A new list.
'''


def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
