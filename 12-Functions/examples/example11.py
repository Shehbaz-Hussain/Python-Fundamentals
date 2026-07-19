"""
File: 12-Functions/examples/example11.py
Topic: Basic Calculator Functions

Description:
This example demonstrates how multiple functions can work together
to perform basic arithmetic operations. Each function is responsible
for one specific task, making the program modular and easier to
maintain.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference of two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient of two numbers."""
    return first_number / second_number


# Input values
number1 = 20
number2 = 5

# Display results
print("First Number :", number1)
print("Second Number:", number2)
print()

print("Addition       :", add(number1, number2))
print("Subtraction    :", subtract(number1, number2))
print("Multiplication :", multiply(number1, number2))
print("Division       :", divide(number1, number2))