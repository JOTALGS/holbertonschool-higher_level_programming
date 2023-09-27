#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem = 0
    if (my_list):
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end='')
                elem += 1
            except ValueError or TypeError:
                pass
    print()
    return (elem)
