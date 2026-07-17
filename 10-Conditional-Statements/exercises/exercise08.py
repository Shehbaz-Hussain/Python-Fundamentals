"""
Exercise 08: Electricity Bill Category Checker

Problem Statement:
Write a Python program that asks the user to enter the monthly electricity
units consumed and displays the billing category.

Billing Categories:
- Less than 100 units       -> Low Consumption
- 100 to 300 units          -> Average Consumption
- More than 300 units       -> High Consumption

Expected Output Examples:

Example 1:
Enter electricity units consumed: 75
Billing Category: Low Consumption

Example 2:
Enter electricity units consumed: 180
Billing Category: Average Consumption

Example 3:
Enter electricity units consumed: 420
Billing Category: High Consumption
"""

# Ask the user to enter the electricity units consumed
units = float(input("Enter electricity units consumed: "))

# Determine the billing category
if units < 100:
    print("Billing Category: Low Consumption")
elif units <= 300:
    print("Billing Category: Average Consumption")
else:
    print("Billing Category: High Consumption")