"""
Exercise 18: Simple Calculator Using Conditional Statements

Problem Statement:
Write a Python program that asks the user to enter two numbers and an
operator. Perform the corresponding arithmetic operation based on the
operator entered.

Supported Operators:
- +  Addition
- -  Subtraction
- *  Multiplication
- /  Division

Conditions:
- If the operator is not one of the supported operators, display an error
  message.
- Before performing division, check that the second number is not zero.

Expected Output Examples:

Example 1:
Enter the first number: 15
Enter the second number: 5
Enter an operator (+, -, *, /): +
Result: 20.0

Example 2:
Enter the first number: 25
Enter the second number: 4
Enter an operator (+, -, *, /): /
Result: 6.25

Example 3:
Enter the first number: 10
Enter the second number: 0
Enter an operator (+, -, *, /): /
Error: Division by zero is not allowed.

Example 4:
Enter the first number: 8
Enter the second number: 2
Enter an operator (+, -, *, /): %
Error: Invalid operator.
"""

# Ask the user to enter the first number
first_number = float(input("Enter the first number: "))

# Ask the user to enter the second number
second_number = float(input("Enter the second number: "))

# Ask the user to enter the operator
operator = input("Enter an operator (+, -, *, /): ")

# Perform the requested operation
if operator == "+":
    print("Result:", first_number + second_number)
elif operator == "-":
    print("Result:", first_number - second_number)
elif operator == "*":
    print("Result:", first_number * second_number)
elif operator == "/":
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
    else:
        print("Result:", first_number / second_number)
else:
    print("Error: Invalid operator.")