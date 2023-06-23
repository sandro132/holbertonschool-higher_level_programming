#!/usr/bin/python3
'''Funtion that appends a string at the end'''


def append_write(filename="", text=""):
    '''open and append the file'''
    with open(filename, "a", encoding="utf-8") as files:
        return files.write(text)
