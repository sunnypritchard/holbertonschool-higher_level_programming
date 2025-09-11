#!/usr/bin/python3
'''
Function:
Prints the first x elements of a list that are integers.
Parameters:
    my_list (list): The list to print elements from.
    x (int): The number of elements to print.
Returns:
    int: The number of integers actually printed.
'''


def safe_print_list_integers(my_list=[], x=0):

    nb_of_int = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            nb_of_int += 1
        except (ValueError, TypeError):
            continue
    print()  # Print a new line after printing the elements
    return nb_of_int


if __name__ == "__main__":

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list_integers(my_list, 2)
    print("nb_print: {:d}".format(nb_print))

    my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
    nb_print = safe_print_list_integers(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))

    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))
