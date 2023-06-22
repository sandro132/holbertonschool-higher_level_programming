#!/usr/bin/python3
'''function that compares the object to the instance and if is an inherited'''


def is_kind_of_class(obj, a_class):
    '''return True if the object is same a instance of a class and inherited'''
    if isinstance(obj, a_class):
        return True
    return False
