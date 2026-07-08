"""
File: example04_string_to_float.py

Topic:
Converting a String to a Float

Description:
This program demonstrates how to convert a string (str)
containing a decimal number into a floating-point number (float)
using the float() function.

Concepts Used:
- Variables
- float()
- print()
- type()
"""

# Store a decimal number as a string
height = "1.75"

# Display the original value
print("Original Value:", height)

# Display the original data type
print("Original Type:", type(height))

print()  # Print a blank line for better readability

# Convert the string to a float
height = float(height)

# Display the converted value
print("Converted Value:", height)

# Display the new data type
print("Converted Type:", type(height))

print()

# Perform a simple calculation
new_height = height + 0.05

print("Height after adding 0.05 meters:", new_height)

"""
Expected Output:

Original Value: 1.75
Original Type: <class 'str'>

Converted Value: 1.75
Converted Type: <class 'float'>

Height after adding 0.05 meters: 1.8
"""