#!/usr/bin/python3
"""Student class Module"""


class Student:
    """Class for students"""

    def __init__(self, first_name, last_name, age):
        """class constructor"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Describe student"""
        if attrs is not None:
            r = {}
            for k, v in self.__dict__.items():
                if k in attrs:
                    r[k] = v
            return r
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v
