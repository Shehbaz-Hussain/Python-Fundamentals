"""
Exercise 10: Shipping Charge Calculator

Problem Statement:
Write a Python program that asks the user to enter the total purchase amount
(in dollars) and determines the shipping charge according to the following
rules:

Shipping Charges:
- Purchase amount less than $50      -> $10 shipping
- Purchase amount from $50 to $99.99 -> $5 shipping
- Purchase amount $100 or more       -> Free shipping

Expected Output Examples:

Example 1:
Enter the purchase amount: 35
Shipping Charge: $10

Example 2:
Enter the purchase amount: 75
Shipping Charge: $5

Example 3:
Enter the purchase amount: 150
Shipping Charge: Free
"""

# Ask the user to enter the purchase amount
purchase_amount = float(input("Enter the purchase amount: $"))

# Determine the shipping charge
if purchase_amount < 50:
    print("Shipping Charge: $10")
elif purchase_amount < 100:
    print("Shipping Charge: $5")
else:
    print("Shipping Charge: Free")