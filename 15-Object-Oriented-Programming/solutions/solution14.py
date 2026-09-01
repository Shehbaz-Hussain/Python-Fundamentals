"""
Solution 14: Method Overriding

Implements exercise14 by defining an Animal parent class and
overriding its speak() method in Dog and Cat subclasses.
"""


class Animal:
    """Represent a general animal."""

    def speak(self):
        """Display a default animal sound."""
        print("Animal makes a sound.")


class Dog(Animal):
    """Represent a dog."""

    def speak(self):
        """Override speak() for a dog."""
        print("Dog says: Woof!")


class Cat(Animal):
    """Represent a cat."""

    def speak(self):
        """Override speak() for a cat."""
        print("Cat says: Meow!")


dog = Dog()
cat = Cat()

dog.speak()
cat.speak()