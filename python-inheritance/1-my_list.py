#!/usr/bin/python3
'''Function that source to list'''


class MyList(list):
    '''class of the list '''
    def print_sorted(self):
        '''print the list sorted'''
        n_list = sorted(self).copy()
        return print(n_list)