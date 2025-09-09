#!/usr/bin/python3
'''
Function:
    multiple_returns(sentence): returns the length and first character of a
    string

Parameters:
    sentence: input string

Returns:
    tuple with the length of the string and its first character
'''


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
