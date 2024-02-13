#!/usr/bin/python3
"""
Module 0-add_integer
"""


def add_integer(a, b=98):
    """
    Adds 2 integers

    Args:
        a: first integer
        b: second integer

    Returns:
        The return value. a + b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b = int(b)
    return a + b
