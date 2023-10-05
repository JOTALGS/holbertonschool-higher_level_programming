#!/usr/bin/python3
"""Base geo#"""


class BaseGeometry:
    "This"
    def area(self):
        """sdass"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """sdadfgg"""
        if not (isinstance(value, int)):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
