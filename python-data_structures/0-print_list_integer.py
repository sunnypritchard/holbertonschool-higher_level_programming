#!/usr/bin/python3
'''
Function:
    print_list_integer(list=[]): prints all integers of a list

Parameters:
    my_list: list of integers

Returns:
    None
'''


def print_list_integer(my_list=[]):
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
