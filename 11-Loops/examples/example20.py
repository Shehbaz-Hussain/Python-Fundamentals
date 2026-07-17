"""
Module: 11-Loops
File: example20.py

Title: Printing a Number Triangle Pattern

Description:
This example demonstrates how nested loops can be used to
create a number pattern.
"""

# Create rows from 1 to 5.
for row in range(1, 6):

    # Print numbers from 1 up to the current row number.
    for number in range(1, row + 1):
        print(number, end=" ")

    # Move to the next line after each row.
    print()