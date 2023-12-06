#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    rs = roman_string
    roman_num = {
            "I": 1, "V": 5, "X": 10,
            "L": 50, "C": 100, "D": 500,
            "M": 1000
    }
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and roman_num[rs[i]] > roman_num[rs[i - 1]]:
            num += roman_num[rs[i]] - 2 * roman_num[rs[i - 1]]
        else:
            num += roman_num[rs[i]]
    return num
