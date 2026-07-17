"""
Exercise 12: Temperature Category Checker

Problem Statement:
Write a Python program that asks the user to enter the current temperature
(in degrees Celsius) and displays the appropriate weather category.

Temperature Categories:
- Less than 0°C          -> Freezing
- 0°C to 15°C            -> Cold
- 16°C to 30°C           -> Pleasant
- Above 30°C             -> Hot

Expected Output Examples:

Example 1:
Enter the temperature (°C): -5
Weather Category: Freezing

Example 2:
Enter the temperature (°C): 10
Weather Category: Cold

Example 3:
Enter the temperature (°C): 24
Weather Category: Pleasant

Example 4:
Enter the temperature (°C): 36
Weather Category: Hot
"""

# Ask the user to enter the temperature
temperature = float(input("Enter the temperature (°C): "))

# Determine the weather category
if temperature < 0:
    print("Weather Category: Freezing")
elif temperature <= 15:
    print("Weather Category: Cold")
elif temperature <= 30:
    print("Weather Category: Pleasant")
else:
    print("Weather Category: Hot")