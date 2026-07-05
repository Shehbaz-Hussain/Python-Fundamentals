"""Example 11: Converting input values to numbers."""

# Read two numbers as strings and convert them to integers
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

# Calculate the sum
result = first_number + second_number

# Display the result
print(f"The sum is: {result}")

# Expected output:
# Enter first number: 8
# Enter second number: 7
# The sum is: 15

# Explanation:
# input() returns a string, so type conversion is required for arithmetic.
