# ==========================================================
# Project: Multiplication Table Generator
# ==========================================================
# Description:
# This program asks the user to enter a number and displays
# its multiplication table from 1 to 10.
#
# Concepts Practiced:
# - Variables
# - Input and Output
# - Type Conversion
# - for Loop
# - range() Function
# ==========================================================

# Ask the user to enter a number
number = int(input("Enter a number: "))

print("\nMultiplication Table\n")

# Display the multiplication table
for multiplier in range(1, 11):
    product = number * multiplier
    print(f"{number} x {multiplier} = {product}")