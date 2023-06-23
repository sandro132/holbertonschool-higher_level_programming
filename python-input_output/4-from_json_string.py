#!/usr/bin/python3
'''Function that return an object'''


import json


def from_json_string(my_obj):
    '''Return object of the json'''
    j_obj = json.loads(my_obj)
    return j_obj
