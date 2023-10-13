#!/usr/bin/python3
"""
    Class Base.
"""
import json


class Base():
    """
        Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
            Initializes a new instance of the Base class.

            Args:
                id (int): An optional ID value.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ddsfvhjfvjh sdsad"""
        if list_dictionaries is not None:
            return json.dumps(list_dictionaries)
        else:
            return "[]"
