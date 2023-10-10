#!/usr/bin/python3
"""dsd"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """sdsdsd"""
    def __init__(self, size):
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.size = size

    def area(self):
        return self.size * self.size
