#!/usr/bin/python3
for i in range(00, 99):
    print("{:02d}".format(i), end=", " if i < 99 else "\n")
