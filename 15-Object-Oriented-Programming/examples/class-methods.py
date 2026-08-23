"""
Topic: Class Methods

Description:
Demonstrates how a class method receives the class as its
first argument and can work with class-level data.
"""


class Student:
    """Represent a student."""

    school = "Python Academy"

    def __init__(self, name):
        """Initialize a student with a name."""
        self.name = name

    @classmethod
    def change_school(cls, new_school):
        """Change the school for the class."""
        cls.school = new_school

    def display_info(self):
        """Display the student's information."""
        print(f"Name: {self.name}")
        print(f"School: {self.school}")


student1 = Student("Ali")
student2 = Student("Ayesha")

student1.display_info()
print()
student2.display_info()

Student.change_school("AI Academy")

print("\nAfter changing the class attribute:")
student1.display_info()
print()
student2.display_info()