#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = set()
    for elements in set_1:
        if elements in set_2:
            new_set.add(elements)
    return new_set
