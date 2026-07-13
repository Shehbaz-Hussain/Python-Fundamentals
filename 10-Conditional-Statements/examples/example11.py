# ============================================================
# Example 11: Using Nested if Statements
# ============================================================
# Description:
# This program demonstrates the use of nested if statements.
# The user must first meet the minimum age requirement.
# If the first condition is True, a second condition checks
# whether the user has a valid driving license.
# ============================================================

# Prompt the user for age
age = int(input("Enter your age: "))

# Check the first condition
if age >= 18:

    # Prompt the user for license status
    has_license = input("Do you have a driving license? (yes/no): ")

    # Check the second condition
    if has_license == "yes":
        print("You are eligible to drive.")
    else:
        print("You are old enough, but you need a valid driving license.")

else:
    print("You are not eligible to drive because you are under 18.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================