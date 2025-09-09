#!/usr/bin/python3
'''
Function:
    add_tuple(tuple_a=(), tuple_b=()): adds two tuples

Parameters:
    tuple_a: first tuple of integers
    tuple_b: second tuple of integers

Returns:
    new tuple with the sums of the elements
'''


def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    return (a[0] + b[0], a[1] + b[1])
