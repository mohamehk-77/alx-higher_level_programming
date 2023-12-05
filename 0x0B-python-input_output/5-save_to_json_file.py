#!/usr/bin/python3
"""module"""

import json


def save_to_json_file(my_obj, filename):
    """func that save obj into file"""
    with open(filename, 'w', encoding='utf-8') as file:
        return json.dump(my_obj, file)
