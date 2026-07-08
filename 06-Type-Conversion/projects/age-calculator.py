"""
File: age-calculator.py

Project: Age Calculator

Difficulty:
Beginner

Description:
This project demonstrates how to use user input, type conversion,
variables, arithmetic operators, and the type() function.

The program asks the user for their:
- Name
- Birth year
- Current year

It converts the year values into integers, calculates the user's age,
and displays the results in a clear format.

Concepts Practiced:
- input()
- print()
- variables
- int()
- str()
- type()
- arithmetic operators (+, -)
"""

# =====================================
# Age Calculator Project
# =====================================

print("=====================================")
print("        AGE CALCULATOR")
print("=====================================")

# Ask the user to enter their name
name = input("Enter your name: ")

# Ask the user to enter the birth year
birth_year_text = input("Enter your birth year: ")

# Ask the user to enter the current year
current_year_text = input("Enter the current year: ")

# Convert the year values to integers
birth_year = int(birth_year_text)
current_year = int(current_year_text)

# Calculate the age
age = current_year - birth_year

print()
print("========== RESULT ==========")

# Display the user's information
print("Name:", str(name))
print("Birth Year:", birth_year)
print("Current Year:", current_year)
print("Age:", age, "years")

print()
print("========== DATA TYPES ==========")

# Display the data types of the variables
print("Name Type:", type(name))
print("Birth Year Type:", type(birth_year))
print("Current Year Type:", type(current_year))
print("Age Type:", type(age))

print()
print("Thank you for using the Age Calculator!")