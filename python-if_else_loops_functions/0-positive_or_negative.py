#!/usr/bin/python3
"""
Generates a random integer between -10 and 10 and prints whether the number is
positive, zero, or negative.
"""
import random
number = random.randint(-10, 10)

if number > 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
else:
    print(f"{number} is negative")
