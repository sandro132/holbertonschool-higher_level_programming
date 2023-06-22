#!/usr/bin/python3
'''function that source to list'''


class MyList(list):
    '''class of the list '''
    def print_sorted(self):
        '''print the list sorted'''
        print(sorted(self))
