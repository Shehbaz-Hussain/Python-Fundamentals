"""
File: 12-Functions/examples/example05.py
Topic: Function with Default Arguments

Description:
This example demonstrates how default arguments work in Python
functions. If a value is not provided when the function is called,
the default value is used automatically. If a value is provided,
it replaces the default value.
"""


# Define a function with a default argument
def greet(name, city="Gilgit"):
    """Display a greeting with a default city."""
    print(f"Hello, {name}!")
    print(f"City: {city}")
    print()


# Function call using the default argument
greet("Ali")

# Function call by providing a different value
greet("Sara", "Lahore")

# Another function call with a custom city
greet("Ahmed", "Karachi")