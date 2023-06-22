#!/usr/bin/python3
'''function that compares the object to the instance'''


def is_same_class(obj, a_class):
    '''return True if the object is same a instance of a class'''
    if obj.__class__ == a_class:
        return True
    return False
