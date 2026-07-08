"""
Project: Shopping Bill Calculator

This program calculates the total shopping bill.
"""

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))

total_bill = item_price * quantity

print("Total Bill:", total_bill)