#!/usr/bin/python3
"""Module demonstrating multiple inheritance with a FlyingFish class."""


class Fish:
    """A class representing a fish."""

    def swim(self):
        """Make the fish swim."""
        print("The fish is swimming")

    def habitat(self):
        """Describe the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A class representing a bird."""

    def fly(self):
        """Make the bird fly."""
        print("The bird is flying")

    def habitat(self):
        """Describe the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish, inheriting from both Fish and Bird."""

    def fly(self):
        """Make the flying fish fly."""
        print("The flying fish is soaring!")

    def swim(self):
        """Make the flying fish swim."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Describe the flying fish's habitat."""
        print("The flying fish lives both in water and the sky!")


# ----- Testing the FlyingFish Class -----
if __name__ == "__main__":
    flying_fish = FlyingFish()
    flying_fish.swim()
    flying_fish.fly()
    flying_fish.habitat()
