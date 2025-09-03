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
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz", end=" ")
        elif number % 3 == 0:
            print("Fizz", end=" ")
        elif number % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
