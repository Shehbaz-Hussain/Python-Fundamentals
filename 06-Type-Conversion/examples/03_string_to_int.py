"""
File: example03_string_to_int.py

Topic:
Converting a String to an Integer

Description:
This program demonstrates how to convert a string (str)
containing a whole number into an integer (int) using
the int() function.

Concepts Used:
- Variables
- int()
- print()
- type()
"""

# Store a number as a string
number = "50"

# Display the original value
print("Original Value:", number)

# Display the original data type
print("Original Type:", type(number))

print()  # Print a blank line for better readability

# Convert the string to an integer
number = int(number)

# Display the converted value
print("Converted Value:", number)

# Display the new data type
print("Converted Type:", type(number))

print()

# Perform arithmetic after conversion
result = number + 25

print("Result after adding 25:", result)

"""
Expected Output:

Original Value: 50
Original Type: <class 'str'>

Converted Value: 50
Converted Type: <class 'int'>

Result after adding 25: 75
"""