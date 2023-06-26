#!/usr/bin/python3
'''import the class base'''

from models.base import Base


'''Rectangle'''


class Rectangle(Base):
    '''Class Resctangle inherited from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    '''Access to width'''
    @property
    def width(self):
        return self.__width

    '''add value to width'''
    @width.setter
    def width(self, value):
        self.__width = value

    '''Access to height'''
    @property
    def height(self):
        return self.__height

    '''add value to height'''
    @height.setter
    def height(self, value):
        self.__height = value

    '''Access to x'''
    @property
    def x(self):
        return self.__x

    '''add value to x'''
    @x.setter
    def x(self, value):
        self.__x = value

    '''Access to y'''
    @property
    def y(self):
        return self.__y

    '''add value to y'''
    @y.setter
    def y(self, value):
        self.__y = value
