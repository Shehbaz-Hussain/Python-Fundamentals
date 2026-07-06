"""
===============================================================================
Project Title : Unit Converter
Repository    : Python-Programming-Foundation
Module        : 05-Input-and-Output
File          : unit-converter.py
Author        : <Your Name>

Description
-----------
This beginner-friendly project performs several common unit conversions.
The program asks the user for values and converts them using standard
conversion formulas.

The program demonstrates how to:
- Accept numeric input from the user
- Convert input strings into floating-point numbers
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
# Create a console application that performs the following independent
# unit conversions:
#
# • Celsius → Fahrenheit
# • Fahrenheit → Celsius
# • Kilometers → Miles
# • Miles → Kilometers
# • Kilograms → Pounds
# • Pounds → Kilograms
# • Centimeters → Inches
# • Inches → Centimeters
#
# The program should ask the user for the required values, perform the
# calculations, and display all results in a clear and well-formatted report.
#
# =============================================================================


# =============================================================================
# Learning Objectives
# =============================================================================
#
# After completing this project, students will be able to:
#
# 1. Receive multiple numeric inputs.
# 2. Convert strings into floating-point numbers.
# 3. Store values in descriptive variables.
# 4. Perform arithmetic using standard conversion formulas.
# 5. Display formatted numeric output.
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
#     - Temperature in Celsius
#     - Temperature in Fahrenheit
#     - Distance in Kilometers
#     - Distance in Miles
#     - Weight in Kilograms
#     - Weight in Pounds
#     - Length in Centimeters
#     - Length in Inches
#
# Step 3:
# Convert all inputs into floating-point numbers.
#
# Step 4:
# Perform all conversions.
#
# Step 5:
# Display the conversion results.
#
# Step 6:
# Display a closing message.
#
# =============================================================================


# =============================================================================
# Complete Python Program
# =============================================================================

print("=" * 70)
print("                    Welcome to the Unit Converter")
print("=" * 70)

print("\nEnter the following values.\n")

# -------------------------------------------------------------------------
# Temperature
# -------------------------------------------------------------------------

celsius = float(input("Temperature (Celsius): "))
fahrenheit = float(input("Temperature (Fahrenheit): "))

# -------------------------------------------------------------------------
# Distance
# -------------------------------------------------------------------------

kilometers = float(input("Distance (Kilometers): "))
miles = float(input("Distance (Miles): "))

# -------------------------------------------------------------------------
# Weight
# -------------------------------------------------------------------------

kilograms = float(input("Weight (Kilograms): "))
pounds = float(input("Weight (Pounds): "))

# -------------------------------------------------------------------------
# Length
# -------------------------------------------------------------------------

centimeters = float(input("Length (Centimeters): "))
inches = float(input("Length (Inches): "))

# -------------------------------------------------------------------------
# Perform Conversions
# -------------------------------------------------------------------------

fahrenheit_result = (celsius * 9 / 5) + 32
celsius_result = (fahrenheit - 32) * 5 / 9

miles_result = kilometers * 0.621371
kilometers_result = miles * 1.60934

pounds_result = kilograms * 2.20462
kilograms_result = pounds / 2.20462

inches_result = centimeters / 2.54
centimeters_result = inches * 2.54

# -------------------------------------------------------------------------
# Display Results
# -------------------------------------------------------------------------

print("\n" + "=" * 70)
print("                     UNIT CONVERSION REPORT")
print("=" * 70)

print(f"{celsius:.2f} °C = {fahrenheit_result:.2f} °F")
print(f"{fahrenheit:.2f} °F = {celsius_result:.2f} °C")

print("-" * 70)

print(f"{kilometers:.2f} km = {miles_result:.2f} miles")
print(f"{miles:.2f} miles = {kilometers_result:.2f} km")

print("-" * 70)

print(f"{kilograms:.2f} kg = {pounds_result:.2f} lb")
print(f"{pounds:.2f} lb = {kilograms_result:.2f} kg")

print("-" * 70)

print(f"{centimeters:.2f} cm = {inches_result:.2f} in")
print(f"{inches:.2f} in = {centimeters_result:.2f} cm")

print("=" * 70)

print("\nThank you for using the Unit Converter!")