#!/usr/bin/python3
""" module """
import json


def load_from_json_file(filename):
    """ func that load from json """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
