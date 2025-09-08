#!/usr/bin/python3
'''
Function:
    print_reversed_list_integer(list=[]): prints all integers of a list,
    in reverse order

Parameters:
    my_list: list of integers

Returns:
    None
'''


def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list) - 1, -1, -1):
        print("{:d}".format(my_list[i]))
