"""
Module: 11-Loops
File: example18.py

Title: Skipping Multiples of Three Using continue

Description:
This example demonstrates how the continue statement can
be used to skip specific values during loop execution.
"""

# Check numbers from 1 to 15.
for number in range(1, 16):

    # Skip numbers divisible by 3.
    if number % 3 == 0:
        continue

    print(number)