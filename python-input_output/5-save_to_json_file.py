#!/usr/bin/python3
'''Function that write an object file, using json'''


import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="utf-8") as files:
        json.dump(my_obj, files)
