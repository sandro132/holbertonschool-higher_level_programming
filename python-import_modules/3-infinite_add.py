#!/usr/bin/python3
import sys
num = sys.argv[1:]
add = 0
if __name__ == '__main__':
    for i in num:
        add += int(i)
    print("{}".format(add))
