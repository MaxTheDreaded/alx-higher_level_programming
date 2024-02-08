#!/usr/bin/python3

"""Defines a MagicClass"""

import math


def MagicClass(radius):
    """Represents a circle"""

    def area(self):
        """Returns the area of the circle"""

        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Returns the circumference of the circle"""

        return 2 * math.pi * self.__radius

    return {'area': area, 'circumference': circumference}
