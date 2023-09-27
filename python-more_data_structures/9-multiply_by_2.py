#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for key in a_dictionary:
        new_dict[key] = 2 * a_dictionary[key]
    return (new_dict)

print_sorted_dictionary = \
    __import__('6-print_sorted_dictionary').print_sorted_dictionary

a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
new_dict = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
