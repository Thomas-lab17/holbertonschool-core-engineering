#!/usr/bin/env python3
"""Defines a Square class with validated size and an area method."""


class Square:
    """Represents a square with controlled access to its size."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): Side length of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """int: Get the side length of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the side length of the square.

        Args:
            value (int): New side length.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
