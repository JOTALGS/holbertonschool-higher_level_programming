#!/usr/bin/python3
def common_elements(set_1, set_2):
    interset = set()
    for element in set_1:
        if element in set_2:
            interset.add(element)
    return (interset)