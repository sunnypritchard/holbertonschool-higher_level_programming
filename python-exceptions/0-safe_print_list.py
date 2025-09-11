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


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))