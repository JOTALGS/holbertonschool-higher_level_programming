#!/usr/bin/python3
"""  5"""


class BaseGeometry:
    """Base Geometry Class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        elif value < 1:
            raise ValueError(f"{name} must be greater than 0")
        else:
            return True
