#!/usr/bin/python3
"""Module demonstrating the use of Abstract Base Classes (ABC) in Python."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal.

    This class defines the interface for all animal subclasses.
    """
    @abstractmethod
    def sound(self):
        """
        Abstract method to be implemented by subclasses to define the sound
        the animal makes.
        """
        pass


class Dog(Animal):
    """Concrete class representing a dog, inheriting from Animal."""
    def sound(self):
        """Implementation of the sound method for Dog."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat, inheriting from Animal."""
    def sound(self):
        """Implementation of the sound method for Cat."""
        return "Meow"


# Test cases to demonstrate functionality:
if __name__ == "__main__":
    def animal_sound(animal: Animal) -> str:
        """Function to get the sound of an animal."""
        return animal.sound()

    dog = Dog()
    cat = Cat()
    print(animal_sound(dog))  # Output: Bark
    print(animal_sound(cat))  # Output: Meow

    bird = Animal()
    print(animal_sound(bird))   # Raises TypeError
