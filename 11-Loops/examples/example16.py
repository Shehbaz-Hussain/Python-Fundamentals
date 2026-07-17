"""
Module: 11-Loops
File: example16.py

Title: Calculating Factorial Using a while Loop

Description:
This example demonstrates how a while loop can be used to
repeat multiplication operations and calculate a factorial.
"""

# Store the number whose factorial will be calculated.
number = 5

# Store the initial result.
factorial = 1

# Store the starting counter value.
counter = 1

# Multiply values from 1 to the given number.
while counter <= number:
    factorial = factorial * counter
    counter = counter + 1

# Display the final factorial value.
print("Factorial:", factorial)