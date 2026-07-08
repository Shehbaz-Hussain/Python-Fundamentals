"""
File: example05_number_to_string.py

Topic:
Converting a Number to a String

Description:
This program demonstrates how to convert a number into
a string using the str() function.

Concepts Used:
- Variables
- str()
- print()
- type()
"""

# Store an integer value
score = 95

# Display the original value
print("Original Value:", score)

# Display the original data type
print("Original Type:", type(score))

print()  # Print a blank line for better readability

# Convert the integer to a string
score = str(score)

# Display the converted value
print("Converted Value:", score)

# Display the new data type
print("Converted Type:", type(score))

print()

# Combine text and the converted string
message = "Your score is " + score

print(message)

"""
Expected Output:

Original Value: 95
Original Type: <class 'int'>

Converted Value: 95
Converted Type: <class 'str'>

Your score is 95
"""