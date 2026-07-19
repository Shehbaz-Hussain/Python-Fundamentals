"""
File: 12-Functions/examples/example02.py
Topic: Function with One Parameter

Description:
This example demonstrates how to define a function that accepts
one parameter. The value is passed to the function when it is
called, allowing the same function to work with different inputs.
"""


# Define a function with one parameter
def greet(name):
    """Display a personalized greeting."""
    print(f"Hello, {name}!")
    print("Welcome to the Python Functions module.")


# Call the function with different arguments
greet("Ali")
print()

greet("Sara")
print()

greet("Ahmed")