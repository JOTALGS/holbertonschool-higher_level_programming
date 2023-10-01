#!/usr/bin/python3


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    trigger_chars = ['.', '?', ':']

    current_line = ""

    for char in text:
        current_line += char

        if char in trigger_chars:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line:
        print(current_line.strip())
