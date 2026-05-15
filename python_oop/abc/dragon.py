#!/usr/bin/env python3
"""
Module demonstrating the use of mixins with a Dragon class.
"""


class SwimMixin:
    """
    Mixin class providing swimming capability.
    """

    def swim(self):
        """
        Print swimming behavior.
        """
        print("The creature swims!")


class FlyMixin:
    """
    Mixin class providing flying capability.
    """

    def fly(self):
        """
        Print flying behavior.
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    Class representing a dragon that can swim and fly.
    """

    def roar(self):
        """
        Print the roaring behavior of the dragon.
        """
        print("The dragon roars!")


if __name__ == "__main__":
    """
    Test the Dragon class and its mixed-in abilities.
    """
    dragon = Dragon()

    dragon.swim()
    dragon.fly()
    dragon.roar()
