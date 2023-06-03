#!/usr/bin/python3
import sys
argv = len(sys.argv) - 1

if __name__ == '__main__':
    if argv == 0:
        print("{} arguments.".format(argv), end="\n")
    elif argv == 1:
        print("{} argument:".format(argv), end="\n")
        print("{}: {}".format(argv, sys.argv[1]), end="\n")
    elif argv > 1:
        print("{} arguments:".format(argv), end="\n")
        for i in range(1, argv + 1):
            print("{}: {}".format(i, sys.argv[i]), end="\n")
