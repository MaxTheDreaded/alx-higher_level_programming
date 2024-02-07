#!/usr/bin/python3

"""Defines a square by: (based on 1-square.py)"""


class Square:
    """Represents a square"""

    def __init__(self, size=0):
        """Initializing this square class
        Args: size - represents the size of the square defined
        """

        self.size = size
        try:
            if type(size) is not int:
                raise TypeError
            if size < 0:
                raise ValueError
            self.__size = size
        except TypeError:
            print("size must be an integer")
        except ValueError:
            print("size must be >= 0")
