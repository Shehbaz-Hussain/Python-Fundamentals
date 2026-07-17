"""
Exercise 04: Voting Eligibility Checker

Problem Statement:
Write a Python program that asks the user to enter their age and determines
whether they are eligible to vote.

Condition:
- A person is eligible to vote if they are 18 years of age or older.

Expected Output Example:

Example 1:
Enter your age: 20
You are eligible to vote.

Example 2:
Enter your age: 16

(No output because only an if statement is used.)
"""

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Check whether the user is eligible to vote
if age >= 18:
    print("You are eligible to vote.")