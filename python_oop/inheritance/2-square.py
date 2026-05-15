#!/usr/bin/env python3
"""
Module that defines the Square class.
"""


Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.

    Attributes:
        __size (int): private size of the square
    """

    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): size of the square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: area of the square
        """
        return self.__size * self.__size

    def __str__(self):
        """
        Return a readable string representation of the square.

        Returns:
            str: formatted string
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
