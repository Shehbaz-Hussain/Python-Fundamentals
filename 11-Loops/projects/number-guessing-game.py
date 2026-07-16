# ==========================================================
# Project: Number Guessing Game
# ==========================================================
# Description:
# This program asks the user to guess a predefined secret
# number. The program continues until the correct number is
# guessed, providing hints after each incorrect attempt.
#
# Concepts Practiced:
# - Variables
# - Input and Output
# - Type Conversion
# - Comparison Operators
# - Conditional Statements
# - while Loop
# - break Statement
# ==========================================================

# Store the secret number
secret_number = 25

print("=== Number Guessing Game ===")
print("Guess the secret number between 1 and 50.")

# Keep asking until the correct number is guessed
while True:
    guess = int(input("\nEnter your guess: "))

    if guess < secret_number:
        print("Too low. Try again.")

    elif guess > secret_number:
        print("Too high. Try again.")

    else:
        print("Congratulations! You guessed the correct number.")
        break

print("\nGame Over.")