"""
Module: 11-Loops
File: example21.py

Title: Calculating the Average of Numbers

Description:
This example demonstrates how a loop can be used to collect
values and perform repeated calculations.
"""

# Store the total value.
total = 0

# Store the number of values.
count = 5

# Add numbers from 1 to 5.
for number in range(1, count + 1):
    total = total + number

# Calculate the average.
average = total / count

# Display the result.
print("Total:", total)
print("Average:", average)