#!/usr/bin/python3
"""class_to_json module"""


import json

def class_to_json(obj):
    """returns the dictionary description with simple data structure"""
    return obj.__dict__
