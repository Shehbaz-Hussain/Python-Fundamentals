# ==========================================================
# Project: Countdown Timer
# ==========================================================
# Description:
# This program asks the user to enter a starting number and
# displays a countdown until it reaches 0.
#
# Concepts Practiced:
# - Variables
# - Input and Output
# - Type Conversion
# - while Loop
# - Comparison Operators
# ==========================================================

print("=== Countdown Timer ===")

# Ask the user to enter the starting number
count = int(input("Enter the starting number: "))

print("\nCountdown:\n")

# Display the countdown
while count >= 0:
    print(count)
    count -= 1

print("\nTime's up!")