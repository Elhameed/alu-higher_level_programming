#!/usr/bin/python3
"""Defines a matrix division function."""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.
    
    Args:
        matrix (list): A list of lists of integers or floats representing the matrix.
        div (int or float): The number to divide all elements of the matrix by.
        
    Returns:
        A new matrix with all elements divided by div and rounded to 2 decimal places.
        
    Raises:
        TypeError: If matrix is not a list of lists of integers or floats, or if div is not a number.
        TypeError: If each row of the matrix is not the same size.
        ZeroDivisionError: If div is 0.
    """
    # Check that matrix is a list of lists of integers or floats
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check that all rows of the matrix have the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check that div is a number and is not 0
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    # Divide all elements of the matrix by div and round to 2 decimal places
    new_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]
    
    return new_matrix
