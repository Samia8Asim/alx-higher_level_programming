#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            new[row][column] = (matrix[row][column] ** 2)
    return new
