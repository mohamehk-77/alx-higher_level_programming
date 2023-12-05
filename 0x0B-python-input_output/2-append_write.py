#!/usr/bin/python3
"""module"""


def append_write(filename="", text=""):
    """func that append a string at the end of file"""
    with open(filename, 'a', encoding='utf-8') as file:
        file.write('\n' + text)
        return file.write(text)
