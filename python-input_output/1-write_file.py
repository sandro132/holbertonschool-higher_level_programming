#!/usr/bin/python3
'''Funtion that writes a string to a tex file'''


def write_file(filename="", text=""):
    '''open and write the file'''
    with open(filename, "w", encoding="utf-8") as files:
        files.write(text)
        return len(text)
