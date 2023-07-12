#!/usr/bin/python3
"""
Task 7: Load, add, save
"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
"""a script that adds all arguments to a Python list, and then save
them to a file"""
file = "add_item.json"
data = load_from_json_file(file)
if data is None:
    data = []
data.extend(sys.argv[1:])
save_to_json_file(data, file)
