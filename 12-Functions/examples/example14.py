"""
File: 12-Functions/examples/example14.py
Topic: Even or Odd Number Checker

Description:
This example demonstrates how a function can determine whether
a number is even or odd. The function returns a value, and the
returned result is displayed to the user.
"""


def check_even_or_odd(number):
    """
    Return whether a number is even or odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


# Sample numbers
first_number = 10
second_number = 17
third_number = 24

# Check each number
print(f"{first_number} is {check_even_or_odd(first_number)}.")
print(f"{second_number} is {check_even_or_odd(second_number)}.")
print(f"{third_number} is {check_even_or_odd(third_number)}.")