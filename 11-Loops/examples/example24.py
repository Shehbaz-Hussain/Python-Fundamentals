"""
Module: 11-Loops
File: example24.py

Title: Checking Prime Number Using a Loop

Description:
This example demonstrates how a loop can be used to check
whether a number is divisible by any value within a range.
"""

# Store the number to check.
number = 7

# Assume the number is prime.
is_prime = True

# Check possible divisors.
for divisor in range(2, number):

    if number % divisor == 0:
        is_prime = False
        break

# Display the result.
if is_prime:
    print("Number is prime.")
else:
    print("Number is not prime.")