#!/usr/bin/python3
"""
Print the last digit of a randomly generated number
"""
import random
number = random.randint(-10000, 10000)
last_digit = number % 10 if number >= 0 else -(abs(number) % 10)

print("Last digit of", end=" ")
if last_digit > 5:
    print(f"{number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{number} is {last_digit} and is 0")
else:
    print(f"{number} is {last_digit} and is less than 6 and not 0")
