#!/usr/bin/python3


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(0, size):
        for _ in range(0, size):
            print("#", end="")
        print()
