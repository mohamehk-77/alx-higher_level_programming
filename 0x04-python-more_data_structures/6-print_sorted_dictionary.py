#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sotr_keys = sorted(a_dictionary.keys())
    for key in sotr_keys:
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
