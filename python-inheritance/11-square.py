#!/usr/bin/python3
'''Import class'''


BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle
Square = __import__('10-square').Square


class Square(Rectangle):
    '''Class Square inherits from Rectangle'''
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)
    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
