#!/usr/bin/python3
def uniq_add(my_list=[]):
    n_set = set(my_list)
    n = 0
    for elem in n_set:
        n += elem
    return (n)
