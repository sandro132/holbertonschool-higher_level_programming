#!/usr/bin/python3
'''Function that create an object from json'''


import json


def load_from_json_file(filename):
    '''open the file and creation'''
    with open(filename, encoding='utf-8') as files:
        return json.load(files)
