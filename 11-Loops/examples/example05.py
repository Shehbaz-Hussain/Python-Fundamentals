"""
Module: 11-Loops
File: example05.py

Title: Calculating the Sum of Numbers from 1 to 10

Description:
This example demonstrates how to use a for loop to perform
repeated calculations and update a variable during each
iteration.
"""

# Store the initial sum value.
total = 0

# Add numbers from 1 to 10.
for number in range(1, 11):
    total = total + number

# Display the final result.
print("Sum:", total)