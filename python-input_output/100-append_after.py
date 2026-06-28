#!/usr/bin/python3
"""Module that defines the append_after function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line after each line containing a specific string.

    Args:
        filename (str): The name of the file to modify.
        search_string (str): The string to search for in each line.
        new_string (str): The string to insert after matching lines.
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()
    result = []
    for line in lines:
        result.append(line)
        if search_string in line:
            result.append(new_string)
    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(result)
