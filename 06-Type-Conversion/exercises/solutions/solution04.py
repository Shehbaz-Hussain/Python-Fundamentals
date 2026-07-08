"""
File: solution04.py

Solution to Exercise 04: Convert a Floating-Point Number to an Integer

This program demonstrates how to convert a floating-point number into
an integer using the int() function.

Note:
The int() function removes the decimal part. It does not round the value.
"""

# Store the floating-point value in a variable
height = 175.9

# Display the original value
print("Original Value:", height)

# Display the original data type
print("Original Type:", type(height))

print()

# Convert the floating-point number to an integer
height_int = int(height)

# Display the converted value
print("Converted Value:", height_int)

# Display the converted data type
print("Converted Type:", type(height_int))