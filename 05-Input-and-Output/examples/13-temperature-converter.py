"""Example 13: Convert Celsius to Fahrenheit."""

# Read the temperature in Celsius
celsius = float(input("Enter temperature in Celsius: "))

# Formula: Fahrenheit = (Celsius × 9/5) + 32
fahrenheit = (celsius * 9 / 5) + 32

# Display the result
print(f"{celsius}°C is equal to {fahrenheit}°F")

# Sample run:
# Enter temperature in Celsius: 25
# 25.0°C is equal to 77.0°F

# Explanation:
# The program reads a temperature in Celsius, converts it to
# Fahrenheit using the standard conversion formula, and displays
# the formatted result.