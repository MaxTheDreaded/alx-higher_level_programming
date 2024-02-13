#!/usr/bin/python3
"""
Module 5-text_indentation
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): text to print
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i in [".", "?", ":"]:
            print(i)
            print()
        else:
            print(i, end="")
