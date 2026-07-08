"""
File: example10_real_world_example.py

Topic:
Real-World Example Using Type Conversion

Description:
This program demonstrates how type conversion is used in a
real-world scenario. It calculates the total cost of shopping
based on the product price and quantity entered by the user.

Concepts Used:
- input()
- int()
- float()
- print()
- Variables
- Basic arithmetic
"""

print("=== Shopping Bill Calculator ===")
print()

# Get product information from the user
product_name = input("Enter the product name: ")

# Convert the price to a float
price = float(input("Enter the price of one item: "))

# Convert the quantity to an integer
quantity = int(input("Enter the quantity: "))

print()

# Calculate the total bill
total_bill = price * quantity

# Display the bill
print("---------- Shopping Bill ----------")
print("Product Name :", product_name)
print("Price        :", price)
print("Quantity     :", quantity)
print("Total Bill   :", total_bill)

"""
Sample Input:

Enter the product name: Notebook
Enter the price of one item: 150.5
Enter the quantity: 3

Expected Output:

=== Shopping Bill Calculator ===

---------- Shopping Bill ----------
Product Name : Notebook
Price        : 150.5
Quantity     : 3
Total Bill   : 451.5
"""