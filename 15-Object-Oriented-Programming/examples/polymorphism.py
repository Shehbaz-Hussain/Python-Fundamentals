"""
Topic: Polymorphism

Description:
Demonstrates polymorphism by using different objects through
the same method interface.
"""


class Dog:
    """Represent a dog."""

    def speak(self):
        """Return the sound made by a dog."""
        print("Dog says: Woof!")


class Cat:
    """Represent a cat."""

    def speak(self):
        """Return the sound made by a cat."""
        print("Cat says: Meow!")


class Cow:
    """Represent a cow."""

    def speak(self):
        """Return the sound made by a cow."""
        print("Cow says: Moo!")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()