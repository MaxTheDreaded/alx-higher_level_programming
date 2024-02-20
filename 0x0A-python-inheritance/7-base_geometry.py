#!/usr/bin/python3
"""
Module base_geometry
"""
"""Defines a class BaseGeometry based on 6-base_geometry."""


class BaseGeometry:
    """Defines a class BaseGeometry."""

    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        """Validate that the method is called with two arguments."""
        args = 1
        if len(locals()) < 3:
            args = len(locals()) - args
            raise TypeError("integer_validator() missing {} required \
            positional arguments: 'name' and 'value'".format(args))
