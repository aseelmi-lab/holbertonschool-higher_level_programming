#!/usr/bin/python3
"""Module that defines the class_to_json function."""


def class_to_json(obj):
    """Returns dictionary description of an object for JSON serialization.

    Args:
        obj: An instance of a class to serialize.

    Returns:
        dict: The dictionary representation of the object.
    """
    return obj.__dict__
