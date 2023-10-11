#!/usr/bin/python3


def add_tuple(tuple_a=(), tuple_b=()):

    new_t = [0, 0]

    for i in range(2):

        if tuple_a is not None:
            if (len(tuple_a) > i):
                new_t[i] = tuple_a[i]

        if tuple_b is not None:
            if (len(tuple_b) > i):
                new_t[i] += tuple_b[i]

    return tuple(new_t)
