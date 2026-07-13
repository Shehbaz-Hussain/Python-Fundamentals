# ============================================================
# Example 20: Student Scholarship Eligibility Checker
# ============================================================
# Description:
# This comprehensive example brings together the concepts
# learned in this module. The program uses comparison
# operators, logical operators, and conditional statements
# to determine whether a student qualifies for a scholarship.
#
# Scholarship Criteria:
# • Marks must be 85 or above.
# • Attendance must be 90% or above.
# ============================================================

# Prompt the user to enter academic information
marks = int(input("Enter your marks: "))
attendance = float(input("Enter your attendance percentage: "))

# Determine scholarship eligibility
if marks >= 85 and attendance >= 90:
    print("Congratulations! You are eligible for the scholarship.")
else:
    print("You are not eligible for the scholarship.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================