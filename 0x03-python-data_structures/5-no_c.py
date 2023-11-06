#!/usr/bin/env python3
def no_c(my_string):
    my_string = ""
    for y in my_string:
        if y != 'c' and y != 'C':
            my_string += y
    return my_string
