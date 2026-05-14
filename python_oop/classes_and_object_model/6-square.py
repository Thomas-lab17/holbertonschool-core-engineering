#!/usr/bin/env python3
"""Defines a Square class with size, position, and printable string form."""


class Square:
    """Represents a square with controlled size and print position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): Side length of the square.
            position (tuple): 2-tuple of non-negative integers (x, y).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
            TypeError: If position is not a tuple of 2 positive integers.
        """
        self.size = size
        self.position = position

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
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """tuple: Get the print position (x, y)."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the print position (x, y).

        Args:
            value (tuple): 2-tuple of non-negative integers.

        Raises:
            TypeError: If value is not a tuple of 2 positive integers.
        """
        if (
            type(value) is not tuple
            or len(value) != 2
            or type(value[0]) is not int
            or type(value[1]) is not int
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integer")

        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using the # character, respecting position."""
        print(str(self))

    def __str__(self):
        """Return the square as a string, using # and respecting position."""
        if self.__size == 0:
            return ""

        lines = []
        for _ in range(self.__position[1]):
            lines.append("")

        row = (" " * self.__position[0]) + ("#" * self.__size)
        for _ in range(self.__size):
            lines.append(row)

        return "\n".join(lines)
