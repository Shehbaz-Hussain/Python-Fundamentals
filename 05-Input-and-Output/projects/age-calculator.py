"""
===============================================================================
Project Title : Age Calculator
Repository    : Python-Programming-Foundation
Module        : 05-Input-and-Output
File          : age-calculator.py
Author        : <Your Name>

Description
-----------
This beginner-friendly project calculates a user's age by subtracting their
birth year from the current year.

The program demonstrates how to:
- Accept numeric input from the user
- Convert input strings into integers
- Perform arithmetic calculations
- Store values in variables
- Display formatted output using f-strings

Concepts Used
-------------
- print()
- input()
- Variables
- Comments
- Basic arithmetic
- Type conversion
- Formatted strings (f-strings)
===============================================================================
"""

# =============================================================================
# Problem Statement
# =============================================================================
#
# Create a console application that asks the user for:
#
# • Birth Year
# • Current Year
#
# Calculate the user's age using the formula:
#
#     Age = Current Year - Birth Year
#
# Display the calculated age in a clean and well-formatted output.
#
# Note:
# This project assumes the birthday has already occurred in the current year.
# The program does not validate user input because conditionals have not yet
# been introduced.
#
# =============================================================================


# =============================================================================
# Learning Objectives
# =============================================================================
#
# After completing this project, students will be able to:
#
# 1. Accept numeric input using input().
# 2. Convert strings into integers using int().
# 3. Store numeric values in variables.
# 4. Perform subtraction.
# 5. Display results using formatted strings.
# 6. Build a simple real-world calculator.
#
# =============================================================================


# =============================================================================
# Algorithm
# =============================================================================
#
# Step 1:
# Display a welcome message.
#
# Step 2:
# Ask the user to enter:
#     - Birth year
#     - Current year
#
# Step 3:
# Convert both inputs into integers.
#
# Step 4:
# Calculate the age.
#
# Step 5:
# Display the entered information.
#
# Step 6:
# Display the calculated age.
#
# Step 7:
# Display a closing message.
#
# =============================================================================


# =============================================================================
# Complete Python Program
# =============================================================================

print("=" * 70)
print("                     Welcome to the Age Calculator")
print("=" * 70)

print("\nPlease enter the following information.\n")

# Get the user's birth year.
birth_year = int(input("Enter your birth year: "))

# Get the current year.
current_year = int(input("Enter the current year: "))

# Calculate the user's age.
age = current_year - birth_year

print("\n" + "=" * 70)
print("                           AGE RESULT")
print("=" * 70)

print(f"Birth Year  : {birth_year}")
print(f"Current Year: {current_year}")
print(f"Age         : {age} years")

print("=" * 70)

print("\nThank you for using the Age Calculator!")