#!/usr/bin/env python3
"""Module implementing shapes with abstract base classes and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """A circle shape defined by its radius."""

    def __init__(self, radius):
        """Initialize the circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Calculate and return the circumference of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """A rectangle shape defined by its width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle with a given width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of any shape using duck typing.

    Does not check the type of the argument explicitly; relies on the
    presence of area() and perimeter() methods on the passed object.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 7)

    print("Circle:")
    shape_info(circle)

    print("\nRectangle:")
    shape_info(rectangle)
