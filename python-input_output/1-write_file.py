#!/usr/bin/python3
""" s """


def write_file(filename="", text="", encoding="utf-8"):
    """sds"""
    with open(filename, "w") as file:
        st = file.write(text)
        file.close()
    return(st)
