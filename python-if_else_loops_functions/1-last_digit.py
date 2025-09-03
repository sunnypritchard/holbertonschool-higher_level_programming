#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10

print("The last digit of", end=" ")
if last_digit > 5:
    print(f"{number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"{number} is {last_digit} and is 0")
elif last_digit < 6 and last_digit != 0:
    if number < 0:
        # Get the last digit of the absolute value and make it negative
        last_digit = -(abs(number) % 10)
        print(f"{number} is {last_digit} and is less than 6 and not 0")
    else:
        print(f"{number} is {last_digit} and is less than 6 and not 0")
