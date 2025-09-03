#!/usr/bin/python3
"""
Functions:
    fizzbuzz: Prints the numbers from 1 to 100, but for multiples of three
    prints "Fizz" instead of the number and for the multiples of five prints
    "Buzz". For numbers which are multiples of both three and five it prints
    "FizzBuzz".
"""


def fizzbuzz():
    for number in range(1, 101):
        print(
            "Fizz" if number % 3 == 0
            else "Buzz" if number % 5 == 0
            else number, end=" " if number != 100 else "\n"
        )
