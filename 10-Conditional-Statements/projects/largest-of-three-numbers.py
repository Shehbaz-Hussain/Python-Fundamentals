"""
Project: Largest of Three Numbers

Description:
This program asks the user to enter three numbers and determines
which one is the largest using conditional statements.

Concepts Used:
- input()
- float()
- if
- elif
- else
- Comparison operators
- Logical operators (and)

Learning Objective:
Understand how multiple conditions can be combined to solve
decision-making problems.
"""

print("===== Largest of Three Numbers =====")

# Get input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Determine the largest number
if number1 >= number2 and number1 >= number3:
    print("\nThe largest number is:", number1)

elif number2 >= number1 and number2 >= number3:
    print("\nThe largest number is:", number2)

else:
    print("\nThe largest number is:", number3)