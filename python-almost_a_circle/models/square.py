#!/usr/bin/python3
'''import'''


from models.rectangle import Rectangle


'''Square'''


class Square(Rectangle):
    '''Class square that inherints from Rectangle'''
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    '''Access to width'''
    @property
    def size(self):
        return self.width

    '''add value to width and height'''
    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        '''overloading the __str__'''
        return '[Square] ({}) {}/{} - {}'\
            .format(self.id, self.x, self.y, self.size)
