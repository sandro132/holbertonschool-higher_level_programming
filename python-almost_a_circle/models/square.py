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

    def update(self, *args, **kwargs):
        '''Method that assign an argument to each'''
        if args:
            if len(args) == 1:
                self.id = args[0]
            if len(args) == 2:
                self.size = args[1]
            if len(args) == 3:
                self.x = args[2]
            if len(args) == 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
