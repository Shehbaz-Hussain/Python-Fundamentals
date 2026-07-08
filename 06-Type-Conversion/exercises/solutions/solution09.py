"""
File: solution09.py

Solution to Exercise 09: Calculate the Area of a Rectangle

This program demonstrates how to:
- Accept user input.
- Convert string input into floating-point numbers.
- Calculate the area of a rectangle.
- Display the result and its data type.

Formula:
Area = Length × Width
"""

# Ask the user to enter the length of the rectangle
length_text = input("Enter the length: ")

# Ask the user to enter the width of the rectangle
width_text = input("Enter the width: ")

# Convert the string inputs into floating-point numbers
length = float(length_text)
width = float(width_text)

# Calculate the area
area = length * width

print()

# Display the entered values
print("Length:", length)
print("Width:", width)

print()

# Display the calculated area
print("Area:", area)

# Display the data type of the area
print("Area Type:", type(area))