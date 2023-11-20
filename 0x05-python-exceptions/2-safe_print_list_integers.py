#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    integer_find = 0
    try:
        for y in range(x):
            print("{:d}".format(my_list[y]), end="")
            integer_find += isinstance(my_list[y], int)
        print()
        return integer_find
    except IndexError:
        print()
        return integer_find
