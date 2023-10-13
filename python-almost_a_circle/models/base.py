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

    @classmethod
    def save_to_file(cls, list_objs):
        """shbb sgah"""
        if "Rectangle" in str(type(list_objs[0])):
            filename = "Rectangle.json"
        else:
            filename = "Square.json"
        with open(filename, 'w', encoding="UTF8") as file:
            if list_objs is None:
                file.write(json.dumps([]))
            for obj in list_objs:
                file.write(json.dumps(obj.__dict__))
            file.close()
