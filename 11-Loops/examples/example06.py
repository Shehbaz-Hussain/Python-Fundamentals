"""
Module: 11-Loops
File: example06.py

Title: Multiplication Table Using a for Loop

Description:
This example demonstrates how to use a for loop with the
range() function to generate a multiplication table.
"""

# Store the number for the multiplication table.
number = 5

# Generate multiplication table from 1 to 10.
for multiplier in range(1, 11):
    result = number * multiplier
    print(number, "x", multiplier, "=", result)