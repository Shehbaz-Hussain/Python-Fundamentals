"""
Exercise 03: Zero Number Checker

Problem Statement:
Write a Python program that asks the user to enter a number and determines
whether the entered number is exactly equal to zero.

Condition:
- If the entered number is equal to 0, display an appropriate message.

Expected Output Example:

Example 1:
Enter a number: 0
The number is zero.

Example 2:
Enter a number: 15

(No output because only an if statement is used.)
"""

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check whether the number is zero
if number == 0:
    print("The number is zero.")