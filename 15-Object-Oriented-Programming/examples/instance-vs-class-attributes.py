"""
Topic: Instance vs Class Attributes

Description:
Demonstrates the difference between instance attributes
and class attributes.
"""


class Student:
    """Represent a student."""

    school = "Python Academy"

    def __init__(self, name):
        """Initialize a student with an instance attribute."""
        self.name = name

    def display_info(self):
        """Display the student's instance and class attributes."""
        print(f"Name: {self.name}")
        print(f"School: {self.school}")


student1 = Student("Ali")
student2 = Student("Ayesha")

student1.display_info()
print()
student2.display_info()

print("\nChanging an instance attribute:")
student1.name = "Ahmed"
student1.display_info()
student2.display_info()

print("\nAccessing the class attribute through the class:")
print(Student.school)