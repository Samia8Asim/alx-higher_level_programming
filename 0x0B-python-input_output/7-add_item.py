#!/usr/bin/python3
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

def add_items_and_save(arg):
    ex_items = load_from_json_file("add_item.json") or []
    ex_items.extend(arg)
    save_to_json_file(ex_items, "add_item.json")


if __name__ == "__main__":
    add_items_and_save(sys.argv[1:])
