#!/usr/bin/python3
"""Locked Class"""


class LockedClass:
    """Locked Class"""
    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """Init method"""
        self.first_name = first_name
