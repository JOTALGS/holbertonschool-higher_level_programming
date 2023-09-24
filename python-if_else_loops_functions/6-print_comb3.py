#!/usr/bin/python3

for first_digit in range(10):
    for second_digit in range(first_digit + 1, 10):
        if first_digit == 8 and second_digit == 9:
            print(f"{first_digit}{second_digit}")
        else:
            print(f"{first_digit}{second_digit}", end=", ")
