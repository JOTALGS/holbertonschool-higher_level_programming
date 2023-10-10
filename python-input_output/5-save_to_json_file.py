#!/usr/bin/python3
"""ds"""
import json


def save_to_json_file(my_obj, filename):
    """jgvjhfhgd"""
    with open(filename, "w", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
