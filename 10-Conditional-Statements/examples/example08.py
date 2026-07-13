# ============================================================
# Example 08: Using an if-elif-else Statement
# ============================================================
# Description:
# This program demonstrates how an if-elif-else statement
# evaluates multiple conditions in sequence. Based on the
# entered marks, the program assigns an appropriate grade.
# ============================================================

# Prompt the user to enter examination marks
marks = int(input("Enter your marks: "))

# Determine the grade
if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
else:
    print("Grade: C")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================