#!/usr/bin/python3
'''function that compares the object to the instance of the class inherited'''


def inherits_from(obj, a_class):
    '''return True if the object is a instance of a class inherited'''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
