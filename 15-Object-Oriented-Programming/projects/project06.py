"""
Project 06: School Management System

Description:
    Demonstrates inheritance, method overriding, super(), and
    polymorphism through a common display_info() interface.
"""


class Person:
    """Represent a general person."""

    def __init__(self, name, age):
        """Initialize a person."""
        self.name = name
        self.age = age

    def display_info(self):
        """Display basic person information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


class Student(Person):
    """Represent a student."""

    def __init__(self, name, age, program):
        """Initialize a student."""
        super().__init__(name, age)
        self.program = program

    def display_info(self):
        """Display student information."""
        super().display_info()
        print(f"Program: {self.program}")


class Teacher(Person):
    """Represent a teacher."""

    def __init__(self, name, age, subject):
        """Initialize a teacher."""
        super().__init__(name, age)
        self.subject = subject

    def display_info(self):
        """Display teacher information."""
        super().display_info()
        print(f"Subject: {self.subject}")


class Administrator(Person):
    """Represent a school administrator."""

    def __init__(self, name, age, department):
        """Initialize an administrator."""
        super().__init__(name, age)
        self.department = department

    def display_info(self):
        """Display administrator information."""
        super().display_info()
        print(f"Department: {self.department}")


people = [
    Student(
        "Ali",
        20,
        "Artificial Intelligence",
    ),
    Teacher(
        "Ayesha",
        35,
        "Python Programming",
    ),
    Administrator(
        "Hamza",
        40,
        "Administration",
    ),
]

print("School Management System")
print("=" * 40)

for person in people:
    person.display_info()
    print()