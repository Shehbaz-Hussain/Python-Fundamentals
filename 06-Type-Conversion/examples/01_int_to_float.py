"""
File: example01_int_to_float.py

Topic:
Converting an Integer to a Float

Description:
This program demonstrates how to convert an integer (int)
into a floating-point number (float) using the float() function.

Concepts Used:
- Variables
- float()
- print()
- type()
"""

# Store an integer value
age = 20

# Display the original value
print("Original Value:", age)

# Display the original data type
print("Original Type:", type(age))

print()  # Print a blank line for better readability

# Convert the integer to a float
age = float(age)

# Display the converted value
print("Converted Value:", age)

# Display the new data type
print("Converted Type:", type(age))

"""
Expected Output:

Original Value: 20
Original Type: <class 'int'>

Converted Value: 20.0
Converted Type: <class 'float'>
"""