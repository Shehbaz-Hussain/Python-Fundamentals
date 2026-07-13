# ============================================================
# Example 14: Checking Access with the Logical OR Operator
# ============================================================
# Description:
# This program demonstrates how the logical OR operator can
# be used in a conditional statement. Access is granted if
# the user has either an administrator account or a moderator
# account.
# ============================================================

# Prompt the user to enter the account role
role = input("Enter your role (admin/moderator/user): ")

# Check whether the user has permission
if role == "admin" or role == "moderator":
    print("Access granted.")
else:
    print("Access denied.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================