#!/usr/bin/python3
'''Function that read a text file UTF8'''


def read_file(filename=""):
    '''open file reads UTF8'''
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
