"""
File: 12-Functions/examples/example09.py
Topic: Local Variables

Description:
This example demonstrates how local variables work in Python.
A local variable is created inside a function and can only be
used within that function. It is not accessible outside the
function.
"""


# Define a function
def display_student():
    """Display student information using local variables."""

    # Local variables
    student_name = "Ali"
    student_age = 20

    print("Student Information")
    print("-------------------")
    print("Name:", student_name)
    print("Age :", student_age)


# Call the function
display_student()

print()

print("The variables 'student_name' and 'student_age'")
print("exist only inside the display_student() function.")