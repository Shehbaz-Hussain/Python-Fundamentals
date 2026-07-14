"""
Project: Login System

Description:
This program simulates a simple login system by asking the user
to enter a username and password. It checks whether the entered
credentials match the predefined values.

Concepts Used:
- input()
- if
- else
- Comparison operators (==)
- Logical operator (and)

Note:
This project is for learning purposes only. Storing usernames
and passwords directly in code is not secure and should not be
used in real-world applications.
"""

print("===== Login System =====")

# Predefined login credentials
correct_username = "admin"
correct_password = "python123"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Validate credentials
if username == correct_username and password == correct_password:
    print("\nLogin successful!")
    print("Welcome,", username)

else:
    print("\nLogin failed.")
    print("Invalid username or password.")