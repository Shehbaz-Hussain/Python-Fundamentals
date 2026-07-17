"""
Module: 11-Loops
File: example17.py

Title: Counting Down with a while Loop and break

Description:
This example demonstrates how the break statement can be
used to stop a while loop when a specific condition is met.
"""

# Starting countdown value.
number = 10

# Continue looping while the number is positive.
while number > 0:

    print(number)

    if number == 5:
        break

    number = number - 1

# Display message after loop termination.
print("Loop stopped.")