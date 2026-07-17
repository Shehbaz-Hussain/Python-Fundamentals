"""
Exercise 16: Discount Calculator

Problem Statement:
Write a Python program that asks the user to enter the total shopping amount
and determines the discount according to the following rules:

Discount Rules:
- Less than $100           -> No Discount
- $100 to $499.99          -> 10% Discount
- $500 to $999.99          -> 20% Discount
- $1000 or more            -> 30% Discount

After determining the discount:
1. Calculate the discount amount.
2. Calculate the final amount to be paid.
3. Display all the results.

Expected Output Examples:

Example 1:
Enter the shopping amount: 80

Original Amount: $80.0
Discount: 0%
Discount Amount: $0.0
Final Amount: $80.0

Example 2:
Enter the shopping amount: 250

Original Amount: $250.0
Discount: 10%
Discount Amount: $25.0
Final Amount: $225.0

Example 3:
Enter the shopping amount: 750

Original Amount: $750.0
Discount: 20%
Discount Amount: $150.0
Final Amount: $600.0
"""

# Ask the user to enter the shopping amount
shopping_amount = float(input("Enter the shopping amount: $"))

# Determine the discount percentage
if shopping_amount < 100:
    discount_percentage = 0
elif shopping_amount < 500:
    discount_percentage = 10
elif shopping_amount < 1000:
    discount_percentage = 20
else:
    discount_percentage = 30

# Calculate the discount amount
discount_amount = shopping_amount * discount_percentage / 100

# Calculate the final payable amount
final_amount = shopping_amount - discount_amount

# Display the results
print("\nOriginal Amount: $", shopping_amount)
print("Discount:", discount_percentage, "%")
print("Discount Amount: $", round(discount_amount, 2))
print("Final Amount: $", round(final_amount, 2))