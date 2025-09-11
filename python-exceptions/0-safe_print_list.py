#!/usr/bin/python3
"""
Function:
Prints x elements of a list.

Parameters:
    my_list (list): The list to print elements from.
    x (int): The number of elements to print.

Returns:
    int: The number of elements actually printed.
"""


def safe_print_list(my_list=[], x=0):

    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()  # Print a new line after printing the elements
    return count

    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()  # Print a new line after printing the elements
    return count
