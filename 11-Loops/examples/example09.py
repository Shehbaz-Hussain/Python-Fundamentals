"""
Module: 11-Loops
File: example09.py

Title: Countdown Using a while Loop

Description:
This example demonstrates how to create a countdown using
a while loop by decreasing the value of a variable in each
iteration.
"""

# Start countdown value.
countdown = 5

# Continue until countdown reaches zero.
while countdown >= 1:
    print(countdown)
    countdown = countdown - 1

# Display completion message.
print("Countdown finished.")