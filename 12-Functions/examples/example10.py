"""
File: 12-Functions/examples/example10.py
Topic: Global Variables

Description:
This example demonstrates how global variables work in Python.
A global variable is defined outside all functions and can be
accessed from inside a function (for reading). Global variables
are available throughout the program.
"""


# Global variable
course_name = "Python Programming Foundation"


# Define a function
def display_course():
    """Display the value of the global variable."""
    print("Course Name:", course_name)


# Main program
print("Accessing a global variable from inside a function:")
display_course()

print()

print("Accessing the same global variable outside the function:")
print("Course Name:", course_name)