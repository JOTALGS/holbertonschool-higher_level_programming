#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = 0
    max_key = ""
    for key in a_dictionary:
        if max_val < a_dictionary[key]:
            max_val = a_dictionary[key]
            max_key = key
    return max_key
