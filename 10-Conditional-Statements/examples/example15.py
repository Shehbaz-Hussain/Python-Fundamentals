# ============================================================
# Example 15: Using the Logical NOT Operator
# ============================================================
# Description:
# This program demonstrates how the logical NOT operator
# reverses the result of a comparison. The program checks
# whether the entered username is not equal to the reserved
# administrator username.
# ============================================================

# Prompt the user to enter a username
username = input("Enter your username: ")

# Check whether the username is different from the reserved name
if not username == "admin":
    print("This username is available.")
else:
    print("The username is reserved. Please choose another one.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================