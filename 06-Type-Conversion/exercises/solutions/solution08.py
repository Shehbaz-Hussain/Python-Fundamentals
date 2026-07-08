"""
File: solution08.py

Solution to Exercise 08: Convert User Input into Different Data Types

This program demonstrates how the same user input can be converted
into different Python data types using:
- int()
- float()
- str()
- bool()

The input() function always returns a string, so explicit type
conversion is required when working with numeric values.
"""

# Ask the user to enter a whole number
number_text = input("Enter a whole number: ")

# Convert the input into different data types
number_int = int(number_text)
number_float = float(number_text)
number_string = str(number_text)
number_boolean = bool(number_text)

print()

# Display the original value and type
print("Original Value:", number_text)
print("Original Type:", type(number_text))

print()

# Display the integer conversion
print("Integer Value:", number_int)
print("Integer Type:", type(number_int))

print()

# Display the floating-point conversion
print("Float Value:", number_float)
print("Float Type:", type(number_float))

print()

# Display the string conversion
print("String Value:", number_string)
print("String Type:", type(number_string))

print()

# Display the Boolean conversion
print("Boolean Value:", number_boolean)
print("Boolean Type:", type(number_boolean))