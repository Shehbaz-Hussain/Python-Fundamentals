"""
Project: Number Classifier

Description:
This program classifies a number based on its value.
It determines whether the number is:
- Positive, Negative, or Zero
- Even or Odd (when the number is not zero)

Concepts Used:
- input()
- int()
- if
- elif
- else
- Nested if statements
- Comparison operators
- Arithmetic operator (%)

Learning Objective:
Practice combining multiple conditional statements to classify
a number based on different conditions.
"""

print("===== Number Classifier =====")

# Get input from the user
number = int(input("Enter an integer: "))

# Classify the number
if number > 0:
    print("\nThe number is Positive.")

    if number % 2 == 0:
        print("It is an Even number.")
    else:
        print("It is an Odd number.")

elif number < 0:
    print("\nThe number is Negative.")

    if number % 2 == 0:
        print("It is an Even number.")
    else:
        print("It is an Odd number.")

else:
    print("\nThe number is Zero.")
    print("Zero is neither Positive nor Negative.")
    print("Zero is an Even number.")