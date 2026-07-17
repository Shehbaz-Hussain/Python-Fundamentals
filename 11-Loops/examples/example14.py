"""
Module: 11-Loops
File: example14.py

Title: Nested for Loop Example

Description:
This example demonstrates how one for loop can be placed
inside another for loop to create repeated combinations.
"""

# Outer loop controls rows.
for row in range(1, 4):

    # Inner loop controls columns.
    for column in range(1, 4):
        print(row, column)