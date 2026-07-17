"""
Exercise 01: Positive Number Checker

Problem Statement:
Write a Python program that asks the user to enter a number and determines
whether the entered number is positive.

Condition:
- If the entered number is greater than zero, display an appropriate message.

Expected Output Examples:

Example 1:
Enter a number: 15
The number is positive.

Example 2:
Enter a number: -7

(No output because only an if statement is used.)
"""

# Ask the user to enter a number
number = int(input("Enter a number: "))

# Check whether the number is positive
if number > 0:
    print("The number is positive.")