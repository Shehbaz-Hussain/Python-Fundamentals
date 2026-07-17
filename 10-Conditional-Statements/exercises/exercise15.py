"""
Exercise 15: Movie Ticket Price Calculator

Problem Statement:
Write a Python program that asks the user for their age and determines the
price of a movie ticket according to the following rules:

Ticket Pricing:
- Age less than 5 years           -> Free
- Age 5 to 12 years               -> $5
- Age 13 to 17 years              -> $8
- Age 18 to 59 years              -> $12
- Age 60 years and above          -> $7 (Senior Citizen Discount)

Expected Output Examples:

Example 1:
Enter your age: 4
Ticket Price: Free

Example 2:
Enter your age: 10
Ticket Price: $5

Example 3:
Enter your age: 16
Ticket Price: $8

Example 4:
Enter your age: 35
Ticket Price: $12

Example 5:
Enter your age: 65
Ticket Price: $7
"""

# Ask the user to enter their age
age = int(input("Enter your age: "))

# Determine the ticket price
if age < 5:
    print("Ticket Price: Free")
elif age <= 12:
    print("Ticket Price: $5")
elif age <= 17:
    print("Ticket Price: $8")
elif age <= 59:
    print("Ticket Price: $12")
else:
    print("Ticket Price: $7")