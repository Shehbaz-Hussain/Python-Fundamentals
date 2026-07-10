# Example 06: Login System
# This program checks whether the entered username
# and password are correct.

correct_username = "admin"
correct_password = "python123"

username = input("Enter username: ")
password = input("Enter password: ")

print()

print("Username entered:", username)
print("Password entered:", password)

is_valid_login = (
    username == correct_username and
    password == correct_password
)

print("Login successful:", is_valid_login)

print("Username is correct:", username == correct_username)
print("Password is correct:", password == correct_password)


# Sample Output:

'''
Enter username: admin
Enter password: hello123

Username entered: admin
Password entered: hello123
Login successful: False
Username is correct: True
Password is correct: False
'''


# Expected Output:

''' 
Enter username: admin
Enter password: python123
Username entered: admin
Password entered: python123
login successful: True
username is correct: True
Password is correct: True
'''



