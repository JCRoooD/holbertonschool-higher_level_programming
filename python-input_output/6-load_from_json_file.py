#!/usr/bin/python3
"""load_from_json_file module"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r', encoding='utf-8') as f:
        import json
        return json.load(f)
