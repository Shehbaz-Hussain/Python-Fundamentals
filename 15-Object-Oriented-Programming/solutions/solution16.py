"""
Solution 16: Polymorphism

Implements exercise16 by creating different classes that
provide the same speak() interface and using their objects
polymorphically.
"""


class Dog:
    """Represent a dog."""

    def speak(self):
        """Display the sound made by a dog."""
        print("Dog says: Woof!")


class Cat:
    """Represent a cat."""

    def speak(self):
        """Display the sound made by a cat."""
        print("Cat says: Meow!")


class Cow:
    """Represent a cow."""

    def speak(self):
        """Display the sound made by a cow."""
        print("Cow says: Moo!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()