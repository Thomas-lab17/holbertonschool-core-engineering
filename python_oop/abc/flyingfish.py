#!/usr/bin/env python3
"""
Module demonstrating multiple inheritance with Fish, Bird, and FlyingFish.
"""


class Fish:
    """
    Class representing a fish.
    """

    def swim(self):
        """
        Print the swimming behavior of a fish.
        """
        print("The fish is swimming")

    def habitat(self):
        """
        Print the habitat of a fish.
        """
        print("The fish lives in water")


class Bird:
    """
    Class representing a bird.
    """

    def fly(self):
        """
        Print the flying behavior of a bird.
        """
        print("The bird is flying")

    def habitat(self):
        """
        Print the habitat of a bird.
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    Class representing a flying fish using multiple inheritance.
    """

    def fly(self):
        """
        Override flying behavior for a flying fish.
        """
        print("The flying fish is soaring!")

    def swim(self):
        """
        Override swimming behavior for a flying fish.
        """
        print("The flying fish is swimming!")

    def habitat(self):
        """
        Override habitat description for a flying fish.
        """
        print("The flying fish lives both in water and the sky!")


if __name__ == "__main__":
    """
    Test the FlyingFish class and demonstrate method resolution order.
    """
    flying_fish = FlyingFish()

    flying_fish.fly()
    flying_fish.swim()
    flying_fish.habitat()

    print("\nMethod Resolution Order:")
    for cls in FlyingFish.mro():
        print(cls)
