#!/usr/bin/python3
"""ds"""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF8") as file:
        file.write(json.dumps(my_obj))
        file.close()
