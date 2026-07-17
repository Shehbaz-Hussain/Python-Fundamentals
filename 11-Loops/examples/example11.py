"""
Module: 11-Loops
File: example11.py

Title: Skipping Numbers Using continue

Description:
This example demonstrates how to use the continue statement
to skip a specific iteration of a loop.
"""

# Print numbers from 1 to 10 except number 5.
for number in range(1, 11):

    if number == 5:
        continue

    print(number)