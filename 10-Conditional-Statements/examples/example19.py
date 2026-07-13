# ============================================================
# Example 19: Determining Discount Eligibility
# ============================================================
# Description:
# This program demonstrates how multiple conditions can be
# combined using logical operators. A customer receives a
# discount if they are a premium member or if their purchase
# amount meets the minimum requirement.
# ============================================================

# Prompt the user for purchase details
purchase_amount = float(input("Enter the purchase amount: "))
is_premium_member = input("Are you a premium member? (yes/no): ")

# Check discount eligibility
if purchase_amount >= 5000 or is_premium_member == "yes":
    print("Congratulations! You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================