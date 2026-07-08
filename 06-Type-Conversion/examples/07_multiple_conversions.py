"""
File: example07_multiple_conversions.py

Topic:
Multiple Type Conversions

Description:
This program demonstrates how to use multiple type
conversion functions in a single program.

Concepts Used:
- Variables
- int()
- float()
- str()
- bool()
- type()
- print()
"""

print("Multiple Type Conversion Example")
print("-" * 35)

# Original values
age_text = "20"
height_text = "1.75"
score = 95
is_registered = 1

# Display original values and their types
print("Original Values")
print("Age:", age_text, "-", type(age_text))
print("Height:", height_text, "-", type(height_text))
print("Score:", score, "-", type(score))
print("Registration:", is_registered, "-", type(is_registered))

print()

# Convert values
age = int(age_text)
height = float(height_text)
score_text = str(score)
registered = bool(is_registered)

# Display converted values and their types
print("Converted Values")
print("Age:", age, "-", type(age))
print("Height:", height, "-", type(height))
print("Score:", score_text, "-", type(score_text))
print("Registration:", registered, "-", type(registered))

"""
Expected Output:

Multiple Type Conversion Example
-----------------------------------

Original Values
Age: 20 - <class 'str'>
Height: 1.75 - <class 'str'>
Score: 95 - <class 'int'>
Registration: 1 - <class 'int'>

Converted Values
Age: 20 - <class 'int'>
Height: 1.75 - <class 'float'>
Score: 95 - <class 'str'>
Registration: True - <class 'bool'>
"""