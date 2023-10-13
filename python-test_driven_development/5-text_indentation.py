#!/usr/bin/python3
"""Module for text_indentation method."""


def text_indentation(text):
    """Method for text_indentation."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] == ' ' and text[i - 1] in [".", "?", ":"]:
            continue
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print("\n")
