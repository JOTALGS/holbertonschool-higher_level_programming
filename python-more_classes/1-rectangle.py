#!/usr/bin/python3
"Rect"


class Rectangle:
    "Tangle"

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height< 0:
            raise ValueError("height must be >= 0")
        self.height = height
