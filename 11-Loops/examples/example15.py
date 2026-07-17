"""
Module: 11-Loops
File: example15.py

Title: Printing a Simple Pattern Using Nested Loops

Description:
This example demonstrates how nested loops can be used to
print a simple pattern.
"""

# Print three rows of stars.
for row in range(1, 4):

    # Print three stars in each row.
    for column in range(1, 4):
        print("*", end="")

    print()