"""
File: example02_float_to_int.py

Topic:
Converting a Float to an Integer

Description:
This program demonstrates how to convert a floating-point
number (float) into an integer (int) using the int() function.

Concepts Used:
- Variables
- int()
- print()
- type()
"""

# Store a floating-point number
price = 99.95

# Display the original value
print("Original Value:", price)

# Display the original data type
print("Original Type:", type(price))

print()  # Print a blank line for better readability

# Convert the float to an integer
price = int(price)

# Display the converted value
print("Converted Value:", price)

# Display the new data type
print("Converted Type:", type(price))

print()
print("Note:")
print("The int() function removes the decimal part.")
print("It does NOT round the number.")

"""
Expected Output:

Original Value: 99.95
Original Type: <class 'float'>

Converted Value: 99
Converted Type: <class 'int'>

Note:
The int() function removes the decimal part.
It does NOT round the number.
"""