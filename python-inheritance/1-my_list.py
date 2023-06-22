#!/usr/bin/python3
''' Documentation'''


class MyList(list):
    '''class of the list '''
    def print_sorted(self):
        '''print the list sorted'''
        n_list = sorted(self).copy()
        print(n_list)
