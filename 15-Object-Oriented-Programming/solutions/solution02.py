"""
Solution 02: Create Multiple Objects

Implements exercise02 by defining a Student class, creating
three Student objects with different names, and displaying
each student's name.
"""


class Student:
    """Represent a student."""

    def __init__(self, name):
        """Initialize a student with a name."""
        self.name = name


student1 = Student("Ali")
student2 = Student("Ayesha")
student3 = Student("Hamza")

print(f"Name: {student1.name}")
print(f"Name: {student2.name}")
print(f"Name: {student3.name}")