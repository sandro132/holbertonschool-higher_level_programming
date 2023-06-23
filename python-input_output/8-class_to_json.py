#!/usr/bin/python3
"""Describe class methods"""


def class_to_json(obj):
    """returns a dictionary"""
    if hasattr(obj, "__dict__"):
        return obj.__dict__
    if hasattr(obj, "__slots__"):
        return obj.__slots__
