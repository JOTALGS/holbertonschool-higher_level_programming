#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_num = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    tot = 0
    prev_value = 0

    for rom in roman_string[::-1]:
        value = roman_num.get(rom, 0)

        if value < prev_value:
            tot -= value
        else:
            tot += value

        prev_value = value

    return tot