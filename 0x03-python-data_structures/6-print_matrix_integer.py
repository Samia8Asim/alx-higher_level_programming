#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for cloumn in row:
            if cloumn != row[2]:
                print("{:d}".format(cloumn), end=" ")
            else:
                print("{:d}".format(cloumn), end="")
        print()
