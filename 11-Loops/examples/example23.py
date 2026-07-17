"""
Module: 11-Loops
File: example23.py

Title: Printing Multiples of a Number

Description:
This example demonstrates how a for loop can be used with
the range() function to generate multiples of a given number.
"""

# Store the number for multiplication.
number = 4

# Print multiples from 1 to 10.
for multiplier in range(1, 11):
    result = number * multiplier
    print(result)