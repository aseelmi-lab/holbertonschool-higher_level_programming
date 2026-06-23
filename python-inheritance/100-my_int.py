#!/usr/bin/python3
"""Module that defines the MyInt class."""


class MyInt(int):
    """Class that inherits from int with inverted == and != operators."""

    def __eq__(self, other):
        """Inverted equality operator.

        Returns:
            bool: True if values are not equal, False if they are.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverted inequality operator.

        Returns:
            bool: True if values are equal, False if they are not.
        """
        return super().__eq__(other)
