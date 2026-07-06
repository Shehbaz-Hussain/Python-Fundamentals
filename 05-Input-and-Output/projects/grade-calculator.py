"""
===============================================================================
Project Title : Grade Calculator
Repository    : Python-Programming-Foundation
Module        : 05-Input-and-Output
File          : grade-calculator.py
Author        : <Your Name>

Description
-----------
This beginner-friendly project collects marks for five subjects and calculates
the total marks, average marks, and percentage.

The program demonstrates how to:
- Accept numeric input from the user
- Convert user input into numbers
- Store values in variables
- Perform arithmetic calculations
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
# Create a console application that asks the user to enter marks for
# the following five subjects:
#
# • English
# • Mathematics
# • Physics
# • Chemistry
# • Computer Science
#
# The program should calculate:
#
# • Total Marks
# • Average Marks
# • Percentage
#
# Display all results in a clean and well-formatted report.
#
# Note:
# This project only performs calculations. It does not assign letter grades
# because conditional statements have not yet been introduced.
#
# =============================================================================


# =============================================================================
# Learning Objectives
# =============================================================================
#
# After completing this project, students will be able to:
#
# 1. Accept multiple numeric inputs.
# 2. Convert strings into floating-point numbers.
# 3. Store values using descriptive variable names.
# 4. Perform arithmetic calculations.
# 5. Calculate totals, averages, and percentages.
# 6. Display formatted reports using f-strings.
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
# Ask the user to enter marks for:
#     - English
#     - Mathematics
#     - Physics
#     - Chemistry
#     - Computer Science
#
# Step 3:
# Convert each input into a floating-point number.
#
# Step 4:
# Calculate:
#     - Total Marks
#     - Average Marks
#     - Percentage
#
# Step 5:
# Display the complete report.
#
# Step 6:
# Display a closing message.
#
# =============================================================================


# =============================================================================
# Complete Python Program
# =============================================================================

print("=" * 70)
print("                   Welcome to the Grade Calculator")
print("=" * 70)

print("\nEnter the marks for the following subjects.\n")

# Collect marks from the user.
english_marks = float(input("English           : "))
mathematics_marks = float(input("Mathematics       : "))
physics_marks = float(input("Physics           : "))
chemistry_marks = float(input("Chemistry         : "))
computer_science_marks = float(input("Computer Science  : "))

# Calculate the total marks.
total_marks = (
    english_marks
    + mathematics_marks
    + physics_marks
    + chemistry_marks
    + computer_science_marks
)

# Calculate the average marks.
average_marks = total_marks / 5

# Assume each subject has a maximum of 100 marks.
maximum_total_marks = 500

# Calculate the percentage.
percentage = (total_marks / maximum_total_marks) * 100

print("\n" + "=" * 70)
print("                        GRADE REPORT")
print("=" * 70)

print(f"English            : {english_marks:.2f}")
print(f"Mathematics        : {mathematics_marks:.2f}")
print(f"Physics            : {physics_marks:.2f}")
print(f"Chemistry          : {chemistry_marks:.2f}")
print(f"Computer Science   : {computer_science_marks:.2f}")

print("-" * 70)

print(f"Total Marks        : {total_marks:.2f} / 500")
print(f"Average Marks      : {average_marks:.2f}")
print(f"Percentage         : {percentage:.2f}%")

print("=" * 70)

print("\nThank you for using the Grade Calculator!")