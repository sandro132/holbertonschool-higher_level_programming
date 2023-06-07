#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        bigger_number = my_list[0]
        for i in my_list:
            if i > bigger_number:
                bigger_number = i
    return bigger_number
