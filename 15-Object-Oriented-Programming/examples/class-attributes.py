"""
Topic: Class Attributes

Description:
Demonstrates how a class attribute is defined on a class
and shared as a class-level value.
"""


class Student:
    """Represent a student."""

    school = "Python Academy"

    def __init__(self, name):
        """Initialize a student with a name."""
        self.name = name

    def display_info(self):
        """Display the student's information."""
        print(f"Name: {self.name}")
        print(f"School: {self.school}")


student1 = Student("Ali")
student2 = Student("Ayesha")

student1.display_info()
print()

student2.display_info()

print(f"\nSchool through class: {Student.school}")