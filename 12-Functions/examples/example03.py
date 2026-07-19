"""
File: 12-Functions/examples/example03.py
Topic: Function with Multiple Parameters

Description:
This example demonstrates how to define a function that accepts
multiple parameters. Each parameter receives a value (argument)
when the function is called, allowing the function to work with
different pieces of information.
"""


# Define a function with two parameters
def introduce_person(name, age):
    """Display a person's name and age."""
    print("Person Information")
    print("------------------")
    print("Name:", name)
    print("Age:", age)
    print()


# Call the function with different arguments
introduce_person("Ali", 20)
introduce_person("Sara", 19)
introduce_person("Ahmed", 22)