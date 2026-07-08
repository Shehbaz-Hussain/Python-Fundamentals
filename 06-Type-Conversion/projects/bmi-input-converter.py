"""
File: bmi-input-converter.py

Project: BMI Input Converter

Difficulty:
Beginner

Description:
This project demonstrates how to use user input, type conversion,
variables, arithmetic operators, and the type() function.

The program asks the user to enter their weight in kilograms and
height in meters, converts the inputs into floating-point numbers,
calculates the Body Mass Index (BMI), and displays the results.

Formula:
BMI = Weight / (Height × Height)

Concepts Practiced:
- input()
- print()
- variables
- float()
- str()
- bool()
- type()
- arithmetic operators (*, /)
"""

# =====================================
# BMI Input Converter Project
# =====================================

print("=====================================")
print("      BMI INPUT CONVERTER")
print("=====================================")

# Ask the user to enter their name
name = input("Enter your name: ")

# Ask the user to enter weight in kilograms
weight_text = input("Enter your weight (kg): ")

# Ask the user to enter height in meters
height_text = input("Enter your height (m): ")

# Convert the string inputs into floating-point numbers
weight = float(weight_text)
height = float(height_text)

# Calculate the Body Mass Index (BMI)
bmi = weight / (height * height)

# Convert the name to a string (demonstration of str())
name_text = str(name)

# Convert the BMI value to a Boolean (demonstration of bool())
bmi_available = bool(bmi)

print()
print("========== RESULT ==========")

# Display the entered information
print("Name:", name_text)
print("Weight:", weight, "kg")
print("Height:", height, "m")
print("BMI:", bmi)

print()
print("========== DATA TYPES ==========")

# Display the data types
print("Name Type:", type(name_text))
print("Weight Type:", type(weight))
print("Height Type:", type(height))
print("BMI Type:", type(bmi))
print("BMI Available:", bmi_available)
print("BMI Available Type:", type(bmi_available))

print()
print("Thank you for using the BMI Input Converter!")