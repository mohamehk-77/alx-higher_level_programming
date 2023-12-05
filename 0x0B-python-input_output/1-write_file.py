#!/usr/bin/python3
"""module"""


def write_file(filename="", text=""):
    """func that write in file"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
        return len(text)
