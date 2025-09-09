#!/usr/bin/python3
'''
Function:
    max_integer(my_list=[]): finds the biggest integer in a list

Parameters:
    my_list: list of integers

Returns:
    biggest integer or None if the list is empty
'''


def max_integer(my_list=[]):

    if not my_list:
        return None

    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
