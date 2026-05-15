#!/usr/bin/env python3
"""
Module that defines the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry shapes.

    This class provides common methods that can be reused
    by subclasses representing specific geometric shapes.
    """

    def area(self):
        """
        Calculate the area of the geometry.

        Raises:
            Exception: If called directly, since it must be
            implemented by subclasses.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that a value is a positive integer.

        Args:
            name (str): The name of the value (used in error messages).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
