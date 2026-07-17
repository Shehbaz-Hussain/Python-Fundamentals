"""
Module: 11-Loops
File: example12.py

Title: Using pass in a Loop

Description:
This example demonstrates how the pass statement can be used
as a placeholder inside a loop without performing any action.
"""

# Loop through numbers from 1 to 5.
for number in range(1, 6):

    if number == 3:
        pass

    print(number)