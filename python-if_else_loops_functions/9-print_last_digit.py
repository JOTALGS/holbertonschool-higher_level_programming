#!/usr/bin/python3
def print_last_digit(number):
    number = str(number)
    print("{}".format(number[-1]),end="")
    return(int(number[-1]))
