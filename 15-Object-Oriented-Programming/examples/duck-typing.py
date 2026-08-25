"""
Topic: Duck Typing

Description:
Demonstrates duck typing by allowing different objects to be
used because they provide the required method.
"""


class Dog:
    """Represent a dog."""

    def speak(self):
        """Make the dog speak."""
        print("Dog says: Woof!")


class Cat:
    """Represent a cat."""

    def speak(self):
        """Make the cat speak."""
        print("Cat says: Meow!")


class Robot:
    """Represent a robot."""

    def speak(self):
        """Make the robot speak."""
        print("Robot says: Hello!")


def make_speak(entity):
    """Call speak() on any object that provides the method."""
    entity.speak()


dog = Dog()
cat = Cat()
robot = Robot()

make_speak(dog)
make_speak(cat)
make_speak(robot)