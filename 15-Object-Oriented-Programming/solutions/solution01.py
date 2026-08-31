"""
Solution 01: Create a Basic Class

Implements exercise01 by defining a Student class, creating
a Student object, and displaying its name.
"""


class Student:
    """Represent a student."""

    def __init__(self, name):
        """Initialize a student with a name."""
        self.name = name


student = Student("Ali")

print(f"Name: {student.name}")