#!/usr/bin/python3
"""dd"""


class Student():
    """fdfd"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def class_to_json(self, obj):
        """fdfd"""
        return obj.__dict__
