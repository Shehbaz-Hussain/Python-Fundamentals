"""
Topic: Objects

Description:
Demonstrates how an object is created from a class and how the
object can be used in a Python program.
"""


class Student:
    """Represent a student."""

    pass


student = Student()

print("Student object:", student)
print("Object type:", type(student))
print("Is student an instance of Student?", isinstance(student, Student))