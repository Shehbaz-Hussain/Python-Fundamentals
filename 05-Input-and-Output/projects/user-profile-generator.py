"""
===============================================================================
Project Title : User Profile Generator
Repository    : Python-Programming-Foundation
Module        : 05-Input-and-Output
File          : user-profile-generator.py
Author        : <Your Name>

Description
-----------
This beginner-friendly project collects basic information from the user and
displays it as a neatly formatted profile using Python's input() and print()
functions.

The program demonstrates how to:
- Accept user input
- Store data in variables
- Display formatted output using f-strings
- Create readable console applications

Concepts Used
-------------
- print()
- input()
- Variables
- Comments
- String concatenation
- Formatted strings (f-strings)
===============================================================================
"""

# =============================================================================
# Problem Statement
# =============================================================================
#
# Create a console application that asks the user for some personal
# information and then displays it in a clean and organized profile.
#
# The program should collect:
#
# • Name
# • Age
# • City
# • Country
# • Favourite Programming Language
#
# The information should be displayed using decorative separators and
# formatted output for better readability.
#
# =============================================================================


# =============================================================================
# Learning Objectives
# =============================================================================
#
# After completing this project, students will be able to:
#
# 1. Use input() to receive information from the keyboard.
# 2. Store user input in variables.
# 3. Display information using print().
# 4. Format output using f-strings.
# 5. Organize console output for better readability.
# 6. Build a simple real-world Python application.
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
#   - Name
#   - Age
#   - City
#   - Country
#   - Favourite Programming Language
#
# Step 3:
# Store each value in a separate variable.
#
# Step 4:
# Display a formatted user profile using decorative separators.
#
# Step 5:
# End the program.
#
# =============================================================================


# =============================================================================
# Complete Python Program
# =============================================================================

print("=" * 70)
print("              Welcome to the User Profile Generator")
print("=" * 70)

print("\nPlease enter the following information.\n")

# Collect user information
name = input("Enter your name: ")

age = input("Enter your age: ")

city = input("Enter your city: ")

country = input("Enter your country: ")

favorite_programming_language = input(
    "Enter your favourite programming language: "
)

print("\n" + "=" * 70)
print("                         USER PROFILE")
print("=" * 70)

print(f"Name                          : {name}")
print(f"Age                           : {age}")
print(f"City                          : {city}")
print(f"Country                       : {country}")
print(
    f"Favourite Programming Language: "
    f"{favorite_programming_language}"
)

print("=" * 70)

print("\nThank you for using the User Profile Generator!")