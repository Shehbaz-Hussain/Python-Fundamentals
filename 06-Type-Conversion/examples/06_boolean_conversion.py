"""
File: example06_boolean_conversion.py

Topic:
Boolean Conversion Using bool()

Description:
This program demonstrates how the bool() function converts
different values into Boolean values (True or False).

Concepts Used:
- Variables
- bool()
- print()
- type()
"""

print("Boolean Conversion Examples")
print("-" * 30)

# Integer values
print("bool(1) =", bool(1))
print("bool(0) =", bool(0))

print()

# Floating-point values
print("bool(3.5) =", bool(3.5))
print("bool(0.0) =", bool(0.0))

print()

# String values
print('bool("Python") =', bool("Python"))
print('bool("") =', bool(""))

print()

# Display the data type of a Boolean value
result = bool(100)

print("Value:", result)
print("Data Type:", type(result))

"""
Expected Output:

Boolean Conversion Examples
------------------------------
bool(1) = True
bool(0) = False

bool(3.5) = True
bool(0.0) = False

bool("Python") = True
bool("") = False

Value: True
Data Type: <class 'bool'>
"""