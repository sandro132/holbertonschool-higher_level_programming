#!/usr/bin/python3
'''Import class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry


'''Function that inherits to BaseGeometry'''


class Rectangle(BaseGeometry):
    '''Class that inherits from BaseGeometry'''
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
