#!/usr/bin/python3

"""Defines a square by: (based on 2-square.py)"""


class Square:
    """Defines a square"""
    def __init__(self, size=0):
        """Initializing this square class
        Args: size - represents the size of the square defined
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size * self.__size
