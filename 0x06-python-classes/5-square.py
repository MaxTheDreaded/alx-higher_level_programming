#!/usr/bin/python3
"""Defines a square by: (based on 4-square.py)"""


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

    @property
    def size(self):
        """Retrieves size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets size to a value"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """Prints in stdout the square with the character #"""
        if self.__size != 0:
            [print("") for i in range(0, self.__size)]
            for i in range(0, self.__size):
                [print("#", end="") for j in range(0, self.__size)]
                print("")
        else:
            print("")
