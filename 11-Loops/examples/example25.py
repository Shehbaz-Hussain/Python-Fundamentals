"""
Module: 11-Loops
File: example25.py

Title: Simple Menu Simulation Using a while Loop

Description:
This example demonstrates how a while loop can repeatedly
execute code until a specific condition is met.
"""

# Store the initial choice value.
choice = 1

# Continue running while the choice is not zero.
while choice != 0:

    print("1. Start Program")
    print("2. View Information")
    print("0. Exit")

    # Simulate a user choice.
    choice = 0

    if choice == 0:
        print("Program exited.")