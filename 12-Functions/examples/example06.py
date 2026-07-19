"""
File: 12-Functions/examples/example06.py
Topic: Keyword Arguments

Description:
This example demonstrates how keyword arguments work in Python.
Instead of relying on the position of arguments, you can specify
the parameter names when calling a function. This improves
readability and allows arguments to be passed in any order.
"""


# Define a function with three parameters
def display_student(name, age, course):
    """Display basic information about a student."""
    print("Student Information")
    print("-------------------")
    print("Name  :", name)
    print("Age   :", age)
    print("Course:", course)
    print()


# Call the function using keyword arguments
display_student(name="Ali", age=20, course="Artificial Intelligence")

# The order of keyword arguments can be changed
display_student(course="Computer Science", name="Sara", age=19)