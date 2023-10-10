#!/usr/bin/python3
"""ds"""
import json
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file



filn = "add_item.json"
with open(filn, "w", encoding="UTF8") as jfil:
    if not os.path.exists(filn):
        ls = []
    else:
        ls = load_from_json_file(filn)
    for i in range(1, len(sys.argv)):
        ls.append(sys.argv[i])
    save_to_json_file(ls, filn)
