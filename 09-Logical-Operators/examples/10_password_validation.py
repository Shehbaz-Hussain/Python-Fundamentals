# Example 10: Password Validation
# This program checks whether the entered password
# matches the correct password.

correct_password = "python123"

entered_password = input("Enter your password: ")

print()

print("Entered Password:", entered_password)

# Check whether the entered password is correct.
is_correct_password = entered_password == correct_password

print("Password is correct:", is_correct_password)

# Check whether the entered password is incorrect.
print("Password is incorrect:", not is_correct_password)


# Sample Output 1:

# Enter your password: python123

# Entered Password: python123
# Password is correct: True
# Password is incorrect: False

# Sample Output 2:

# Enter your password: hello123

# Entered Password: hello123
# Password is correct: False
# Password is incorrect: True

# Sample Output 3:

# Enter your password: Python123

# Entered Password: Python123
# Password is correct: False
# Password is incorrect: True