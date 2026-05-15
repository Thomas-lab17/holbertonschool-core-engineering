#!/usr/bin/env python3
"""
Module defining an abstract Animal class and its subclasses Dog and Cat.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Abstract base class representing an animal.
    """

    @abstractmethod
    def sound(self):
        """
        Produce the sound made by the animal.

        Returns:
            str: The sound of the animal.
        """
        pass


class Dog(Animal):
    """
    Class representing a dog.
    """

    def sound(self):
        """
        Return the sound made by a dog.

        Returns:
            str: The sound "Bark".
        """
        return "Bark"


class Cat(Animal):
    """
    Class representing a cat.
    """

    def sound(self):
        """
        Return the sound made by a cat.

        Returns:
            str: The sound "Meow".
        """
        return "Meow"
