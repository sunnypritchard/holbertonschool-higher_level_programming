#!/usr/bin/python3
'''
Function:
    roman_to_int(roman_string):
        Converts a Roman numeral to an integer.
Parameters:
    roman_string: the Roman numeral to convert.
Returns:
    The converted integer.
'''


def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for c in reversed(roman_string):
        if c not in roman_numerals:
            return 0
        value = roman_numerals[c]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
