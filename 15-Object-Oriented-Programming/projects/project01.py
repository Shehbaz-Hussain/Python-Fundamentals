"""
Project 01: Student Management System

Description:
    Demonstrates classes, objects, instance attributes, instance
    methods, self, initialization, and object state management.
"""


class Student:
    """Represent a student."""

    def __init__(self, name, age, program):
        """Initialize a student."""
        self.name = name
        self.age = age
        self.program = program

    def display_info(self):
        """Display student information."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Program: {self.program}")

    def update_program(self, new_program):
        """Update the student's academic program."""
        self.program = new_program


student1 = Student(
    "Ali",
    20,
    "Artificial Intelligence",
)

student2 = Student(
    "Ayesha",
    21,
    "Computer Science",
)

student3 = Student(
    "Hamza",
    22,
    "Software Engineering",
)

students = [student1, student2, student3]

print("Student Management System")
print("=" * 35)

for student in students:
    student.display_info()
    print()

print("Updating Ali's program...")
student1.update_program("Machine Learning")

print("\nUpdated Student Information")
print("=" * 35)

for student in students:
    student.display_info()
    print()