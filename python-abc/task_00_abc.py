#!/usr/bin/python3
"""Module that defines Animal abstract class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract class that defines an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method that returns the sound of the animal."""
        pass


class Dog(Animal):
    """Class that defines a dog, inherits from Animal."""

    def sound(self):
        """Returns the sound a dog makes."""
        return "Bark"


class Cat(Animal):
    """Class that defines a cat, inherits from Animal."""

    def sound(self):
        """Returns the sound a cat makes."""
        return "Meow"
