# ============================================================
# Example 10: Checking Leap Year Eligibility Rule
# ============================================================
# Description:
# This example demonstrates how multiple conditions can be
# evaluated using an if-elif-else statement. For simplicity,
# this program checks only the basic rule that a year must be
# divisible by 4 to be considered a leap year.
#
# Note:
# The complete leap year algorithm involves additional rules,
# which will be covered later when more Python concepts have
# been learned.
# ============================================================

# Prompt the user to enter a year
year = int(input("Enter a year: "))

# Check whether the year satisfies the basic leap year rule
if year % 4 == 0:
    print(year, "is a leap year based on the basic rule.")
else:
    print(year, "is not a leap year based on the basic rule.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================