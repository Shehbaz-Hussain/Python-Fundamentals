# ============================================================
# Example 12: Combining Comparison and Logical Operators
# ============================================================
# Description:
# This program demonstrates how comparison operators and
# logical operators can be used together in a single
# conditional statement. A student passes only if the marks
# are within the valid range and meet the passing criteria.
# ============================================================

# Prompt the user to enter marks
marks = int(input("Enter your marks (0-100): "))

# Check whether the marks are valid and the student has passed
if marks >= 50 and marks <= 100:
    print("Result: Pass")
elif marks >= 0 and marks < 50:
    print("Result: Fail")
else:
    print("Invalid marks entered.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================