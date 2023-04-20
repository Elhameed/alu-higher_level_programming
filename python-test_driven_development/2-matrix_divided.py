#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list): lists of integers or floats representing the matrix.
        div (int/float): number to divide all elements of the matrix by.

    Returns:
        A new matrix with all elements divided and rounded to 2 d.p.

    Raises:
        TypeError: If matrix is not a list of ints/floats,
        TypeError: If each row of the matrix is not the same size.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, (list,)):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")
    for row in matrix:
        if type(row) != list:
            raise TypeError("matrix must be a matrix "
                            "(list of lists) of integers/floats")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError("matrix must be a matrix"
                                " (list of lists) of integers/floats")
    common_size = len(matrix[0])
    for row in matrix:
        if len(row) != common_size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for i in range(len(matrix)):
        new_matrix.append(list())
        for j in range(len(matrix[i])):
            new_matrix[i].append(round(matrix[i][j] / div, 2))
    return new_matrix
