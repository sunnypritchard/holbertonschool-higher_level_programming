#!/usr/bin/python3
'''
Function:
    divisible_by_2(my_list=[]): checks if elements in a list are divisible by 2

Parameters:
    my_list: list of integers

Returns:
    list of boolean values indicating divisibility by 2
'''


def divisible_by_2(my_list=[]):
    return [num % 2 == 0 for num in my_list]
