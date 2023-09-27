#!/usr/bin/python3
def roman_to_int(roman_string):
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

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))