"""
File: solution10.py

Solution to Exercise 10: Calculate Body Mass Index (BMI)

This program demonstrates how to:
- Accept user input.
- Convert string input into floating-point numbers.
- Perform arithmetic operations.
- Calculate the Body Mass Index (BMI).
- Display the result and its data type.

Formula:
BMI = Weight / (Height × Height)

Note:
This program calculates only the BMI value. It does not classify
the BMI (such as underweight, normal, overweight, etc.) because
conditional statements have not been introduced yet.
"""

# Ask the user to enter their weight in kilograms
weight_text = input("Enter your weight (kg): ")

# Ask the user to enter their height in meters
height_text = input("Enter your height (m): ")

# Convert the string inputs into floating-point numbers
weight = float(weight_text)
height = float(height_text)

# Calculate the Body Mass Index (BMI)
bmi = weight / (height * height)

print()

# Display the entered values
print("Weight:", weight, "kg")
print("Height:", height, "m")

print()

# Display the calculated BMI
print("BMI:", bmi)

# Display the data type of the BMI
print("BMI Type:", type(bmi))