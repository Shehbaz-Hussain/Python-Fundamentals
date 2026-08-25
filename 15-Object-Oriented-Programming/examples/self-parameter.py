"""
Topic: The self Parameter

Description:
Demonstrates how the self parameter refers to the current
instance inside instance methods.
"""


class Student:
    """Represent a student."""

    def __init__(self, name, age):
        """Initialize a student with a name and age."""
        self.name = name
        self.age = age

    def introduce(self):
        """Display information about the student."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


student = Student("Ali", 20)

student.introduce()