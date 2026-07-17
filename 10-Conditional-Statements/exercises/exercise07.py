"""
Exercise 07: Number Classifier

Problem Statement:
Write a Python program that asks the user to enter a number and determines
whether the number is:
- Positive
- Negative
- Zero

Expected Output Examples:

Example 1:
Enter a number: 25
The number is positive.

Example 2:
Enter a number: -8
The number is negative.

Example 3:
Enter a number: 0
The number is zero.
"""

# Ask the user to enter a number
number = float(input("Enter a number: "))

# Check whether the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")