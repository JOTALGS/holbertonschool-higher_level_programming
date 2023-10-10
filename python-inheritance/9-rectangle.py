#!/usr/bin/python3
"""sdsd"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """sdsda"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        return (f"[Rectangle] {self.width}/{self.height}")
