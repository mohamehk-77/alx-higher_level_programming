#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        tries = 0
        for y in range(x):
            print("{}".format(my_list[y]), end="")
            tries += 1
        print()
        return tries
    except IndexError:
        print()
        return tries
