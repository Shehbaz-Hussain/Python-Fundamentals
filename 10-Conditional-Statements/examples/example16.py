# ============================================================
# Example 16: Determining Whether a Year is Eligible to Vote
# ============================================================
# Description:
# This program combines comparison and logical operators to
# determine whether a person is eligible to vote. The user
# must satisfy both conditions to be considered eligible.
# ============================================================

# Prompt the user for required information
age = int(input("Enter your age: "))
citizenship = input("Are you a citizen? (yes/no): ")

# Check voting eligibility
if age >= 18 and citizenship == "yes":
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================