"""
File: solution06.py

Solution to Exercise 06: Calculate the Total Cost of Two Items

This program demonstrates how to:
- Accept user input.
- Convert string input into floating-point numbers.
- Perform arithmetic operations.
- Display the resulting value and its data type.
"""

# Ask the user to enter the price of the first item
price1_text = input("Enter the price of the first item: ")

# Ask the user to enter the price of the second item
price2_text = input("Enter the price of the second item: ")

# Convert the string inputs to floating-point numbers
price1 = float(price1_text)
price2 = float(price2_text)

# Calculate the total cost
total_cost = price1 + price2

print()

# Display the entered prices
print("Price of Item 1:", price1)
print("Price of Item 2:", price2)

print()

# Display the total cost
print("Total Cost:", total_cost)

# Display the data type of the total cost
print("Total Type:", type(total_cost))