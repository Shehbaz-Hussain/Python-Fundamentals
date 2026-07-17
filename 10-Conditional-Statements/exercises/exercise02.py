"""
Exercise 02: Negative Number Checker

Problem Statement:
Write a Python program that asks the user to enter a number and determines
whether the entered number is negative.

Condition:
- If the entered number is less than zero, display an appropriate message.

Expected Output Examples:

Example 1:
Enter a number: -8
The number is negative.

Example 2:
Enter a number: 12

(No output because only an if statement is used.)
"""

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check whether the number is negative
if number < 0:
    print("The number is negative.")