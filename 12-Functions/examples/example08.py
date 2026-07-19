"""
File: 12-Functions/examples/example08.py
Topic: Multiple Function Calls

Description:
This example demonstrates how multiple functions can be defined
and called from the same program. Each function performs a
specific task, making the code easier to organize, read, and
reuse.
"""


# Define the first function
def display_line():
    """Display a separator line."""
    print("-" * 30)


# Define the second function
def welcome():
    """Display a welcome message."""
    print("Welcome to the Python Functions module!")


# Define the third function
def goodbye():
    """Display a closing message."""
    print("Thank you for learning Python Functions!")


# Program execution starts here
display_line()
welcome()
display_line()

print("This program contains multiple function calls.")

display_line()
goodbye()
display_line()