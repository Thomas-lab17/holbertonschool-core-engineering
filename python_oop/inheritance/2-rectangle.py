#!/usr/bin/env python3
"""
Module that defines the Rectangle class.
"""


BaseGeometry = __import__('base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle class that inherits from BaseGeometry.

    Attributes:
        __width (int): private width of the rectangle
        __height (int): private height of the rectangle
    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance.

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a readable string representation of the rectangle.

        Returns:
            str: formatted string
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
