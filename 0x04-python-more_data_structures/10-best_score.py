#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    max_score = None
    for key in a_dictionary:
        if max_score is None:
            max_score = a_dictionary[key]
        elif max_score < a_dictionary[key]:
            max_score = a_dictionary[key]
    for key in a_dictionary:
        if max_score == a_dictionary[key]:
            return key
