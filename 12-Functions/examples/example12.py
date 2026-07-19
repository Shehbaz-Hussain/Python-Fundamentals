"""
File: 12-Functions/examples/example12.py
Topic: Area Calculation Using Functions

Description:
This example demonstrates how functions can be used to calculate
the area of different shapes. Each function performs one specific
calculation, making the code organized, reusable, and easy to
understand.
"""


def calculate_rectangle_area(length, width):
    """Return the area of a rectangle."""
    return length * width


def calculate_square_area(side):
    """Return the area of a square."""
    return side * side


# Given dimensions
rectangle_length = 10
rectangle_width = 5
square_side = 6

# Calculate areas
rectangle_area = calculate_rectangle_area(
    rectangle_length,
    rectangle_width
)

square_area = calculate_square_area(square_side)

# Display results
print("Rectangle")
print("---------")
print("Length:", rectangle_length)
print("Width :", rectangle_width)
print("Area  :", rectangle_area)

print()

print("Square")
print("------")
print("Side:", square_side)
print("Area:", square_area)