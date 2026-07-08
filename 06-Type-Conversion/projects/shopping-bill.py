"""
File: shopping-bill.py

Project: Shopping Bill Calculator

Difficulty:
Beginner

Description:
This project demonstrates how to use user input, type conversion,
variables, arithmetic operators, and the type() function.

The program asks the user to enter the prices of three shopping items,
converts the inputs into floating-point numbers, calculates the total
bill, and displays the results.

Concepts Practiced:
- input()
- print()
- variables
- float()
- str()
- type()
- arithmetic operators (+)
"""

# =====================================
# Shopping Bill Calculator Project
# =====================================

print("=====================================")
print("     SHOPPING BILL CALCULATOR")
print("=====================================")

# Ask the user to enter the price of the first item
item1_text = input("Enter the price of Item 1: ")

# Ask the user to enter the price of the second item
item2_text = input("Enter the price of Item 2: ")

# Ask the user to enter the price of the third item
item3_text = input("Enter the price of Item 3: ")

# Convert the inputs into floating-point numbers
item1_price = float(item1_text)
item2_price = float(item2_text)
item3_price = float(item3_text)

# Calculate the total shopping bill
total_bill = item1_price + item2_price + item3_price

print()
print("========== RESULT ==========")

# Display the prices
print("Item 1 Price:", item1_price)
print("Item 2 Price:", item2_price)
print("Item 3 Price:", item3_price)

print()

# Display the total bill
print("Total Bill:", total_bill)

print()
print("========== DATA TYPES ==========")

# Display the data types
print("Item 1 Type:", type(item1_price))
print("Item 2 Type:", type(item2_price))
print("Item 3 Type:", type(item3_price))
print("Total Bill Type:", type(total_bill))

print()
print("Thank you for using the Shopping Bill Calculator!")