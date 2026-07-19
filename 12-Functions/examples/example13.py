"""
File: 12-Functions/examples/example13.py
Topic: Temperature Conversion Using Functions

Description:
This example demonstrates how functions can be used to convert
temperatures between Celsius and Fahrenheit. Each function performs
one conversion, making the program modular, reusable, and easy to
maintain.
"""


def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius


# Sample values
temperature_celsius = 25
temperature_fahrenheit = 86

# Perform conversions
converted_fahrenheit = celsius_to_fahrenheit(temperature_celsius)
converted_celsius = fahrenheit_to_celsius(temperature_fahrenheit)

# Display results
print("Temperature Conversion")
print("----------------------")

print(
    f"{temperature_celsius}°C = "
    f"{converted_fahrenheit:.1f}°F"
)

print(
    f"{temperature_fahrenheit}°F = "
    f"{converted_celsius:.1f}°C"
)