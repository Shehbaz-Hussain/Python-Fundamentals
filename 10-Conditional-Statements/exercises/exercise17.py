"""
Exercise 17: Login Authentication System

Problem Statement:
Write a Python program that asks the user to enter a username and password.
Check whether the entered credentials are correct.

Login Rules:
- Correct Username: admin
- Correct Password: python123

Conditions:
- If both username and password are correct, display a welcome message.
- If the username is incorrect, display an appropriate message.
- If the username is correct but the password is incorrect, display an
  appropriate message.

Expected Output Examples:

Example 1:
Enter username: admin
Enter password: python123
Login successful.
Welcome, admin!

Example 2:
Enter username: admin
Enter password: hello123
Incorrect password.

Example 3:
Enter username: ali
Enter password: python123
Username not found.
"""

# Ask the user to enter the username
username = input("Enter username: ")

# Ask the user to enter the password
password = input("Enter password: ")

# Check the login credentials
if username == "admin":
    if password == "python123":
        print("Login successful.")
        print("Welcome, admin!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")