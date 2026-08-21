"""
Topic: Instance Attributes

Description:
Demonstrates how individual objects can store their own data
through instance attributes.
"""


class Student:
    """Represent a student."""

    def set_details(self, name, age):
        """Store student details as instance attributes."""
        self.name = name
        self.age = age


student_one = Student()
student_two = Student()

student_one.set_details("Ali", 20)
student_two.set_details("Sara", 21)

print("Student 1:", student_one.name, student_one.age)
print("Student 2:", student_two.name, student_two.age)