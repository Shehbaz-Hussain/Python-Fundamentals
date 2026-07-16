# ==========================================================
# Project: Password Attempt System
# ==========================================================
# Description:
# This program allows the user a limited number of attempts
# to enter the correct password. The program stops when the
# correct password is entered or when all attempts have been
# used.
#
# Concepts Practiced:
# - Variables
# - Input and Output
# - while Loop
# - Conditional Statements
# - Comparison Operators
# - break Statement
# ==========================================================

# Store the correct password
correct_password = "Python123"

# Maximum number of attempts
maximum_attempts = 3
attempt = 1

print("=== Password Attempt System ===")

# Allow the user to enter the password
while attempt <= maximum_attempts:
    entered_password = input("Enter the password: ")

    if entered_password == correct_password:
        print("\nAccess granted. Welcome!")
        break

    remaining_attempts = maximum_attempts - attempt

    if remaining_attempts > 0:
        print(f"\nIncorrect password. Attempts remaining: {remaining_attempts}")
    else:
        print("\nAccess denied. No attempts remaining.")

    attempt += 1

print("\nProgram finished.")