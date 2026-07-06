"""
===============================================================================
Project Title : BMI Calculator
Repository    : Python-Programming-Foundation
Module        : 05-Input-and-Output
File          : bmi-calculator.py
Author        : <Your Name>

Description
-----------
This beginner-friendly project calculates a person's Body Mass Index (BMI)
using their weight and height.

The program demonstrates how to:
- Accept numeric input from the user
- Convert input strings into numbers
- Perform arithmetic calculations
- Display formatted output using f-strings
- Round numerical values for better readability

Concepts Used
-------------
- print()
- input()
- Variables
- Comments
- Basic arithmetic
- Type conversion
- f-strings
===============================================================================
"""

# =============================================================================
# Problem Statement
# =============================================================================
#
# Create a console application that asks the user for:
#
# • Weight (in kilograms)
# • Height (in meters)
#
# Calculate the Body Mass Index (BMI) using the formula:
#
#     BMI = weight / (height ** 2)
#
# Display the calculated BMI rounded to two decimal places.
#
# Note:
# This project only calculates BMI. It does not classify the BMI because
# conditional statements have not been introduced yet.
#
# =============================================================================


# =============================================================================
# Learning Objectives
# =============================================================================
#
# After completing this project, students will be able to:
#
# 1. Receive numeric input from the keyboard.
# 2. Convert user input into floating-point numbers.
# 3. Perform arithmetic calculations.
# 4. Use the exponent operator (**).
# 5. Display decimal numbers using formatted strings.
# 6. Build a practical real-world calculator.
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
#     - Weight in kilograms
#     - Height in meters
#
# Step 3:
# Convert both inputs to floating-point numbers.
#
# Step 4:
# Calculate BMI.
#
# Step 5:
# Display the entered information.
#
# Step 6:
# Display the calculated BMI rounded to two decimal places.
#
# Step 7:
# End the program.
#
# =============================================================================


# =============================================================================
# Complete Python Program
# =============================================================================

print("=" * 70)
print("                     Welcome to the BMI Calculator")
print("=" * 70)

print("\nPlease enter the following information.\n")

# Get the user's weight in kilograms.
weight = float(input("Enter your weight (kg): "))

# Get the user's height in meters.
height = float(input("Enter your height (m): "))

# Calculate Body Mass Index (BMI).
bmi = weight / (height ** 2)

print("\n" + "=" * 70)
print("                           BMI RESULT")
print("=" * 70)

print(f"Weight : {weight:.2f} kg")
print(f"Height : {height:.2f} m")
print(f"BMI    : {bmi:.2f}")

print("=" * 70)

print("\nThank you for using the BMI Calculator!")