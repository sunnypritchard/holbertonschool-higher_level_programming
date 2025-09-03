#!/usr/bin/python3
"""
Print numbers 0 to 99
"""
for number in range(0, 100):
    print("{:02}".format(number), end=", " if number < 99 else "\n")
