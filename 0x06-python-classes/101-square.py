#!/usr/bin/python3

"""Defines a square by: (based on 6-square.py)"""


class Square:
    """Defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the object with the given size and position.

        Parameters:
            size (int): The size of the object.
            position (tuple): The position of the object as a
              tuple of (x, y) coordinates.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position"""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not all(isinstance(i, int) for i in value)
            or any(i < 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square"""
        return self.size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.size == 0:
            print()
        else:
            for _ in range(self.position[1]):
                print()
            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
