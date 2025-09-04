#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args_sum = 0
    for i in range(1, len(argv)):
        args_sum += int(argv[i])
    print("{}".format(args_sum))
