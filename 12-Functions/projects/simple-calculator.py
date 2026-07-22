"""
Project: Simple Calculator

Description:
This project demonstrates how functions can be used to organize
a simple calculator program. Each arithmetic operation is
performed by a separate function.
"""


def add(first_number, second_number):
    """Return the sum of two numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """Return the difference of two numbers."""
    return first_number - second_number


def multiply(first_number, second_number):
    """Return the product of two numbers."""
    return first_number * second_number


def divide(first_number, second_number):
    """Return the quotient of two numbers."""
    if second_number == 0:
        return "Division by zero is not allowed."

    return first_number / second_number


def main():
    """Run the calculator program."""
    first_number = float(input("Enter the first number: "))
    second_number = float(input("Enter the second number: "))

    print("\nResults")
    print("-------")
    print(f"Addition: {add(first_number, second_number)}")
    print(f"Subtraction: {subtract(first_number, second_number)}")
    print(f"Multiplication: {multiply(first_number, second_number)}")
    print(f"Division: {divide(first_number, second_number)}")


main()