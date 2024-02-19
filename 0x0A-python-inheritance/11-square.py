#!/usr/bin/python3

"""Defines a Square class that inherits from Rectangle."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the Square."""
        return self.__size ** 2

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
