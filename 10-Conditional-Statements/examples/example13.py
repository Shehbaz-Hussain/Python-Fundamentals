# ============================================================
# Example 13: Checking Login Credentials
# ============================================================
# Description:
# This program demonstrates how multiple conditions can be
# combined using the logical AND operator. Access is granted
# only when both the username and password are correct.
# ============================================================

# Prompt the user to enter login credentials
username = input("Enter your username: ")
password = input("Enter your password: ")

# Verify the credentials
if username == "admin" and password == "python123":
    print("Login successful.")
else:
    print("Invalid username or password.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================