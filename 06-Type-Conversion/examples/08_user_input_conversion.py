"""
File: example08_user_input_conversion.py

Topic:
User Input Conversion

Description:
This program demonstrates how to convert user input into
the correct data types before performing calculations.

Concepts Used:
- input()
- int()
- float()
- print()
- type()
- Variables
"""

print("=== User Input Conversion Example ===")

# Get user's name (no conversion needed)
name = input("Enter your name: ")

# Get user's age and convert it to an integer
age = int(input("Enter your age: "))

# Get user's height and convert it to a float
height = float(input("Enter your height (in meters): "))

print()

# Display the collected information
print("----- User Information -----")
print("Name:", name)
print("Age:", age)
print("Height:", height)

print()

# Display the data types
print("----- Data Types -----")
print("Name:", type(name))
print("Age:", type(age))
print("Height:", type(height))

print()

# Perform a simple calculation
next_year_age = age + 1

print("Next Year Your Age Will Be:", next_year_age)

"""
Sample Input:

Enter your name: Ali
Enter your age: 20
Enter your height (in meters): 1.75

Expected Output:

=== User Input Conversion Example ===

----- User Information -----
Name: Ali
Age: 20
Height: 1.75

----- Data Types -----
Name: <class 'str'>
Age: <class 'int'>
Height: <class 'float'>

Next Year Your Age Will Be: 21
"""