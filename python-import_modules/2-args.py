#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = len(argv) - 1

    if args == 1:
        print("{} argument:".format(args))
        print("{}: {}".format(args, argv[1]))
    elif args > 1:
        print("{} arguments:".format(args))
        for i in range(1, args + 1):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments.".format(args))
