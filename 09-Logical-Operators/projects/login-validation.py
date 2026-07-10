# Project: Login Validation
# ----------------------------------------
# Objective:
# Validate a user's login credentials using
# logical operators.
#
# Concepts Used:
# - Variables
# - Input and Output
# - Comparison Operators
# - Logical Operators (and)
#
# Note:
# This project only uses concepts covered
# up to Module 09.

print("===== Login Validation System =====")

correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

print()

login_successful = (
    username == correct_username and
    password == correct_password
)

print("Username Entered :", username)
print("Password Entered :", password)

print()

print("Username Correct :", username == correct_username)
print("Password Correct :", password == correct_password)

print()

print("Login Successful :", login_successful)


# Sample Output 1:

# ===== Login Validation System =====
# Enter username: admin
# Enter password: python123

# Username Entered : admin
# Password Entered : python123

# Username Correct : True
# Password Correct : True

# Login Successful : True

# Sample Output 2:

# ===== Login Validation System =====
# Enter username: admin
# Enter password: hello123

# Username Entered : admin
# Password Entered : hello123

# Username Correct : True
# Password Correct : False

# Login Successful : False

# Sample Output 3:

# ===== Login Validation System =====
# Enter username: user
# Enter password: python123

# Username Entered : user
# Password Entered : python123

# Username Correct : False
# Password Correct : True

# Login Successful : False