"""
File: currency-input-calculator.py

Project: Currency Input Calculator

Difficulty:
Beginner

Description:
This project demonstrates how to use user input, type conversion,
variables, arithmetic operators, and the type() function.

The program asks the user to enter:
- Amount in Pakistani Rupees (PKR)
- Exchange rate (PKR for 1 USD)

It converts both inputs into floating-point numbers, calculates the
equivalent amount in US Dollars (USD), and displays the results.

Formula:
USD = PKR / Exchange Rate

Concepts Practiced:
- input()
- print()
- variables
- float()
- str()
- type()
- arithmetic operators (+, -, *, /)
"""

# =====================================
# Currency Input Calculator Project
# =====================================

print("=====================================")
print("   CURRENCY INPUT CALCULATOR")
print("=====================================")

# Ask the user to enter the amount in PKR
pkr_text = input("Enter the amount in PKR: ")

# Ask the user to enter the exchange rate
exchange_rate_text = input("Enter the exchange rate (PKR for 1 USD): ")

# Convert the inputs to floating-point numbers
pkr = float(pkr_text)
exchange_rate = float(exchange_rate_text)

# Calculate the equivalent amount in USD
usd = pkr / exchange_rate

print()
print("========== RESULT ==========")

# Display the converted currency
print("Amount in PKR:", pkr)
print("Exchange Rate:", exchange_rate)
print("Equivalent Amount in USD:", usd)

print()
print("========== DATA TYPES ==========")

# Display the data types
print("PKR Type:", type(pkr))
print("Exchange Rate Type:", type(exchange_rate))
print("USD Type:", type(usd))

print()
print("Thank you for using the Currency Input Calculator!")