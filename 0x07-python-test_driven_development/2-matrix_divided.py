#!/usr/bin/python3
"""Module of function matrix_divided"""


def matrix_divided(matrix, div):
    """Function to divide all elements of a matrix
    Args:
        matrix: input matrix
        div: number to divide by
    Raises:
        TypeError: if matrix not  list of lists of int or floats
        TypeError: if row of the matrix not all of the same size
        TypeError: if div not a number
        ZeroDivisionError: if div == 0
    Return:
        list: new matrix
    """
    if div == 0:
        raise ZeroDivisionError("Division by zero")

    if not isinstance(div, (float, int)):
        raise TypeError("div must be a number")

    if not all(
        isinstance(r, list) and all(isinstance(num, (int, float))\
        for num in r) for r in matrix
    ):
        raise TypeError("Matrix must be a matrix (list of lists) "
                        "of integers/floats")

    if any(len(r)) != len(matrix[0]) for r in matrix:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(num / div, 2) for num in r] for r in matrix]
    return new_matrix


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
