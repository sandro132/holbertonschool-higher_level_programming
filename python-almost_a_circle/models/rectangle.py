#!/usr/bin/python3
'''import the class base'''

from models.base import Base


'''Rectangle'''


class Rectangle(Base):
    '''Class Resctangle inherited from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    '''Access to width'''
    @property
    def width(self):
        return self.__width

    '''add value to width'''
    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    '''Access to height'''
    @property
    def height(self):
        return self.__height

    '''add value to height'''
    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    '''Access to x'''
    @property
    def x(self):
        return self.__x

    '''add value to x'''
    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    '''Access to y'''
    @property
    def y(self):
        return self.__y

    '''add value to y'''
    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.__width * self.__height
