#!/usr/bin/python3
def uppercase(str):
    new_string = ""
    for i in str:
        if 'a' <= i <= 'z':
            new_string += chr((ord(i) - ord('a')) + ord('A'))
        else:
            new_string += i
    print("{}".format(new_string))
