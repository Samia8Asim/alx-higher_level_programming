#!/usr/bin/python3
"""Pascal’s triangle"""


def pascal_triangle(n):
    from math import factorial as fac
    pas_list = []
    if n <= 0:
        return pas_list
    for i in range(n):
        row = [1] * (i + 1)
        if i > 1:
            for j in range(1, i):
                row[j] = pas_list[i-1][j-1] + pas_list[i-1][j]
        pas_list.append(row)
    return pas_list
