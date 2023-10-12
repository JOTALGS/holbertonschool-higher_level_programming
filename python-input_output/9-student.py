#!/usr/bin/python3
"""dd"""


class Student():
    """fdfd"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """fdfd"""
        new_dic = {}
        if attrs is not None:
            for att in attrs:
                if att in self.__dict__.keys():
                    new_dic[att] = self.__dict__[att]
            return new_dic
        else:
            return self.__dict__
