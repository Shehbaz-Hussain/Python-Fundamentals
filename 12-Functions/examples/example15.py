"""
File: 12-Functions/examples/example15.py
Topic: Finding the Maximum of Two Numbers

Description:
This example demonstrates how a function can compare two numbers
and return the larger one. It shows how functions can be used to
encapsulate decision-making logic and return a useful result.
"""


def find_maximum(first_number, second_number):
    """
    Return the larger of two numbers.
    If both numbers are equal, return either one.
    """
    if first_number >= second_number:
        return first_number
    return second_number


# Sample values
number1 = 45
number2 = 78

# Call the function
largest_number = find_maximum(number1, number2)

# Display the result
print("First Number :", number1)
print("Second Number:", number2)
print("Largest Number:", largest_number)