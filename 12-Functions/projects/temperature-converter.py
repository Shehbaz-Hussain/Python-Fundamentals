"""
Project: Temperature Converter

Description:
This project demonstrates how functions can be used to convert
temperatures between Celsius and Fahrenheit.
"""


def celsius_to_fahrenheit(celsius):
    """Return the temperature in Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Return the temperature in Celsius."""
    return (fahrenheit - 32) * 5 / 9


def main():
    """Run the temperature converter."""
    print("Temperature Converter")
    print("---------------------")

    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = celsius_to_fahrenheit(celsius)

    print(f"\n{celsius:.2f}°C = {fahrenheit:.2f}°F")

    fahrenheit = float(input("\nEnter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)

    print(f"{fahrenheit:.2f}°F = {celsius:.2f}°C")


main()