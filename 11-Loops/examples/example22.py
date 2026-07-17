"""
Module: 11-Loops
File: example22.py

Title: Counting Digits in a Number Using a while Loop

Description:
This example demonstrates how a while loop can be used to
repeat an operation until a condition becomes false.
"""

# Store the number.
number = 12345

# Store the digit counter.
digit_count = 0

# Count digits by removing one digit in each iteration.
while number > 0:
    number = number // 10
    digit_count = digit_count + 1

# Display the total number of digits.
print("Number of digits:", digit_count)