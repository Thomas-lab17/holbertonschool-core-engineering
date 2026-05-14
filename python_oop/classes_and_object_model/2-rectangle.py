#!/usr/bin/env python3
"""Defines a Rectangle class with area and perimeter behavior."""


class Rectangle:
    """Represents a rectangle with controlled width and height."""

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle.

        Args:
            width (int): The rectangle width.
            height (int): The rectangle height.

        Raises:
            TypeError: If width or height is not an integer.
            ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """int: Get the rectangle width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the rectangle width.

        Args:
            value (int): New width.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: Get the rectangle height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the rectangle height.

        Args:
            value (int): New height.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Return the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the rectangle perimeter.

        If either width or height is 0, perimeter is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
