"""
File: solution05.py

Solution to Exercise 05: Convert Values to Boolean

This program demonstrates how the bool() function converts different
values into Boolean values.

Rules:
- 0 becomes False.
- Non-zero numbers become True.
- An empty string ("") becomes False.
- A non-empty string becomes True.
"""

# Store different values in variables
value1 = 0
value2 = 15
value3 = ""
value4 = "Python"

# Convert each value to a Boolean
boolean_value1 = bool(value1)
boolean_value2 = bool(value2)
boolean_value3 = bool(value3)
boolean_value4 = bool(value4)

# Display the results for Value 1
print("Value 1:", value1)
print("Original Type:", type(value1))
print("Boolean Value:", boolean_value1)
print("Boolean Type:", type(boolean_value1))

print()

# Display the results for Value 2
print("Value 2:", value2)
print("Original Type:", type(value2))
print("Boolean Value:", boolean_value2)
print("Boolean Type:", type(boolean_value2))

print()

# Display the results for Value 3
print("Value 3:", value3)
print("Original Type:", type(value3))
print("Boolean Value:", boolean_value3)
print("Boolean Type:", type(boolean_value3))

print()

# Display the results for Value 4
print("Value 4:", value4)
print("Original Type:", type(value4))
print("Boolean Value:", boolean_value4)
print("Boolean Type:", type(boolean_value4))