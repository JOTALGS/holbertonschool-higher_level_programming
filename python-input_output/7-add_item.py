#!/usr/bin/python3
"""ds"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """jgvjhfhgd"""
    filn = "add_item.json"
    if not os.path.exists(filn):
        ls = []
    else:
        ls = load_from_json_file(filn)
    for i in range(1, len(sys.argv)):
        ls.append(sys.argv[i])
    save_to_json_file(ls, filn)


if __name__ == "__main__":
    main()
