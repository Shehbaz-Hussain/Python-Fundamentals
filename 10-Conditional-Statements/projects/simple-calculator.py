"""
Project: Simple Calculator

Description:
This program performs a basic arithmetic operation based on the
operator entered by the user.

Concepts Used:
- input()
- float()
- if
- elif
- else
- Comparison operators
- Conditional statements

Supported Operations:
+  Addition
-  Subtraction
*  Multiplication
/  Division
"""

print("===== Simple Calculator =====")

# Get input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("\nAvailable Operators")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

operator = input("\nEnter an operator (+, -, *, /): ")

if operator == "+":
    result = number1 + number2
    print("Result:", result)

elif operator == "-":
    result = number1 - number2
    print("Result:", result)

elif operator == "*":
    result = number1 * number2
    print("Result:", result)

elif operator == "/":
    if number2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = number1 / number2
        print("Result:", result)

else:
    print("Invalid operator. Please enter +, -, *, or /.")