"""
Solution 17: Duck Typing

Implements exercise17 by defining different classes that
provide the required speak() behavior without sharing a
parent class.
"""


class Dog:
    """Represent a dog."""

    def speak(self):
        """Display the dog's message."""
        print("Dog says: Woof!")


class Robot:
    """Represent a robot."""

    def speak(self):
        """Display the robot's message."""
        print("Robot says: Hello!")


class Person:
    """Represent a person."""

    def speak(self):
        """Display the person's message."""
        print("Person says: Hello!")


def make_speak(entity):
    """Call speak() on any object that provides the method."""
    entity.speak()


dog = Dog()
robot = Robot()
person = Person()

make_speak(dog)
make_speak(robot)
make_speak(person)