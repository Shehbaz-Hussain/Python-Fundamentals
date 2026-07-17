"""
Module: 11-Loops
File: example13.py

Title: Using Loop else with for Loop

Description:
This example demonstrates how the else block of a for loop
executes when the loop completes without using break.
"""

# Search through numbers from 1 to 5.
target_number = 8

for number in range(1, 6):

    print("Checking:", number)

    if number == target_number:
        print("Number found.")
        break

else:
    print("Number was not found.")