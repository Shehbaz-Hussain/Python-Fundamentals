"""
File: 12-Functions/examples/example04.py
Topic: Function Returning a Value

Description:
This example demonstrates how a function can return a value using
the `return` statement. The returned value can be stored in a
variable, displayed, or used in other expressions.
"""


# Define a function that returns a value
def add_numbers(first_number, second_number):
    """Return the sum of two numbers."""
    total = first_number + second_number
    return total


# Call the function and store the returned value
result = add_numbers(15, 25)

# Display the result
print("First Number :", 15)
print("Second Number:", 25)
print("Sum          :", result)