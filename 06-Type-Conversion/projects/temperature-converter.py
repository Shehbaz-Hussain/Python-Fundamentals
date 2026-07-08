"""
File: temperature-converter.py

Project: Temperature Converter

Difficulty:
Beginner

Description:
This project demonstrates how to use user input, type conversion,
variables, arithmetic operators, and the type() function.

The program asks the user to enter a temperature in degrees Celsius,
converts it to a floating-point number, calculates the equivalent
temperature in degrees Fahrenheit, and displays the results.

Formula:
Fahrenheit = (Celsius × 9 / 5) + 32

Concepts Practiced:
- input()
- print()
- variables
- float()
- str()
- type()
- arithmetic operators (+, *, /)
"""

# =====================================
# Temperature Converter Project
# =====================================

print("=====================================")
print("    TEMPERATURE CONVERTER")
print("=====================================")

# Ask the user to enter a temperature in Celsius
celsius_text = input("Enter the temperature in Celsius: ")

# Convert the input to a floating-point number
celsius = float(celsius_text)

# Calculate the temperature in Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

print()
print("========== RESULT ==========")

# Display the temperatures
print("Temperature in Celsius:", celsius, "°C")
print("Temperature in Fahrenheit:", fahrenheit, "°F")

print()
print("========== DATA TYPES ==========")

# Display the data types
print("Celsius Type:", type(celsius))
print("Fahrenheit Type:", type(fahrenheit))

print()
print("Thank you for using the Temperature Converter!")