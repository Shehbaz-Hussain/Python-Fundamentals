"""
File: 12-Functions/examples/example19.py
Topic: Nested Function Calls

Description:
This example demonstrates nested function calls, where the return
value of one function is passed directly as an argument to another
function. This technique helps combine small, reusable functions
to perform more complex tasks.
"""


def add(number1, number2):
    """Return the sum of two numbers."""
    return number1 + number2


def multiply(number1, number2):
    """Return the product of two numbers."""
    return number1 * number2


def display_result(value):
    """Display the final result."""
    print("Final Result:", value)


# Nested function call
display_result(multiply(add(5, 3), 4))