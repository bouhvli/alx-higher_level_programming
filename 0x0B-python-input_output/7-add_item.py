#!/usr/bin/python3
"""
Task 0: read file and print it
"""
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
import sys

file  = "add_item.json"
try:
    data = load_from_json_file(file)
except:
    data = None

if data is None:
    data = []
data.extend(sys.argv[1:])
save_to_json_file(data, file)