#!/usr/bin/python3
"""Base geo#"""


class BaseGeometry:
    "This"
    def area(self):
        """sdass"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """sdadfgg"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value < 1:
            raise ValueError(f"{name} must be greater than 0")
