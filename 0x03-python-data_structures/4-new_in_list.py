#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if 0 <= idx < len(my_list):
        copy_list = my_list[:]
        copy_list[idx] = element
        return copy_list
    else:
        return my_list
