#!/usr/bin/python3
"""sd"""


def append_write(filename="", text=""):
    """sds"""
    with open(filename, "a", encoding="utf-8") as file:
        st = file.write(text)
        file.close()
    return(st)
