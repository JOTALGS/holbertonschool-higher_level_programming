#!/usr/bin/python3
"""Class that defines a square"""


class Square:
    """Not Empty Class"""
    def __init__(self, size=0):
        try:
            int(size)
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        except TypeError:
            raise TypeError("size must be an integer")
