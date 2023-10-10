#!/usr/bin/python3
"""
Module for project Base class.
The “base” class to manage id attribute across subclasses
and to avoid duplicating the same code.
"""


class Base:
    """
    Representation of Base class.

    Attrs:
        id: An ID for instances.

    Class attrs:
        __nb_objects: Keeps count of the number of instances created.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialises Base class obj with an ID.

        Args:
            id (int, optional): An ID for the instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
