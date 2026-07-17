"""
Exercise 05: Even or Odd Number Checker

Problem Statement:
Write a Python program that asks the user to enter an integer and determines
whether the entered number is even or odd.

Conditions:
- If the number is divisible by 2, it is an even number.
- Otherwise, it is an odd number.

Expected Output Examples:

Example 1:
Enter an integer: 24
The number is even.

Example 2:
Enter an integer: 17
The number is odd.
"""

# Ask the user to enter an integer
number = int(input("Enter an integer: "))

# Check whether the number is even or odd
if number % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")