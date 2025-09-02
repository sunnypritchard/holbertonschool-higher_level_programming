#!/usr/bin/python3
"""
This module demonstrates string slicing by extracting parts of the word 'Holberton'.
It prints the first 3 letters, last 2 letters, and the middle part of the word.
"""
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
print(f"First 3 letters: {word_first_3}")
print(f"Last 2 letters: {word_last_2}")
print(f"Middle word: {middle_word}")
