#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    num_unique = set()
    for num in my_list:
        if num not in num_unique:
            num_unique.add(num)
            result += num
    return result
