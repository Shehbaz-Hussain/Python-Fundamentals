"""
Exercise 11: Income Tax Category Checker

Problem Statement:
Write a Python program that asks the user to enter their annual income and
determines the applicable tax category.

Tax Categories:
- Less than $20,000          -> No Tax
- $20,000 to $49,999         -> Low Tax
- $50,000 to $99,999         -> Medium Tax
- $100,000 or more           -> High Tax

Expected Output Examples:

Example 1:
Enter your annual income: 18000
Tax Category: No Tax

Example 2:
Enter your annual income: 45000
Tax Category: Low Tax

Example 3:
Enter your annual income: 85000
Tax Category: Medium Tax

Example 4:
Enter your annual income: 120000
Tax Category: High Tax
"""

# Ask the user to enter their annual income
income = float(input("Enter your annual income: $"))

# Determine the tax category
if income < 20000:
    print("Tax Category: No Tax")
elif income < 50000:
    print("Tax Category: Low Tax")
elif income < 100000:
    print("Tax Category: Medium Tax")
else:
    print("Tax Category: High Tax")