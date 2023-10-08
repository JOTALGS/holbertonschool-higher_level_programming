#!/usr/bin/python3
""" s """


def write_file(filename="", text=""):
    """sds"""
    with open(filename, "w", encoding="utf-8") as file:
        st = file.write(text)
        file.close()
    return(st)
