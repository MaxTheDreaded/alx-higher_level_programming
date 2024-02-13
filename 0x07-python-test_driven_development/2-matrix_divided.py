#!/usr/bin/python3
"""
Module 2-matrix_divided
"""


def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix

    Args:
        matrix: list of lists
        div: divisor

    Raises:
        TypeError: if the matrix contains non-numbers
        TypeError: if the matrix contains rows of different sizes
        TypeError: if div is not an integer or float
        ZeroDivisionError: if div is 0

    Returns:
        New matrix
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of \
                        integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    return [[round(num / div, 2) for num in row] for row in matrix]
