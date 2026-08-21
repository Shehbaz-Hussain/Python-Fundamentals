"""
Topic: Multiple Objects

Description:
Demonstrates how multiple independent objects can be created from
the same class.
"""


class Student:
    """Represent a student."""

    pass


student_one = Student()
student_two = Student()
student_three = Student()

print("Student 1:", student_one)
print("Student 2:", student_two)
print("Student 3:", student_three)

print("Student 1 and Student 2 are the same object:", student_one is student_two)
print("Student 2 and Student 3 are the same object:", student_two is student_three)