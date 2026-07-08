"""
File: solution02.py

Solution to Exercise 02: Convert a String to a Floating-Point Number

This program demonstrates how to convert a string into a floating-point
number using the float() function.
"""

# Store the string value in a variable
price_text = "99.95"

# Display the original value
print("Original Value:", price_text)

# Display the original data type
print("Original Type:", type(price_text))

print()

# Convert the string to a floating-point number
price = float(price_text)

# Display the converted value
print("Converted Value:", price)

# Display the converted data type
print("Converted Type:", type(price))