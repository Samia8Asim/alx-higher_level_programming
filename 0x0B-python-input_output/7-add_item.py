#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
argl = list(sys.argv[1:])

try:
    ex_items = load_from_json_file("add_item.json")
except Exception:
    ex_items = []
ex_items.extend(argl)
save_to_json_file(ex_items, "add_item.json")
