"""
Module: 11-Loops
File: example10.py

Title: Finding a Number Using break

Description:
This example demonstrates how to use the break statement
to stop a loop when a specific value is found.
"""

# Search for the target number.
target_number = 7

# Check numbers from 1 to 10.
for number in range(1, 11):

    print("Checking:", number)

    if number == target_number:
        print("Number found!")
        break