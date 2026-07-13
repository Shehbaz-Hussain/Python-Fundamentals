# ============================================================
# Example 17: Identifying the Largest of Three Numbers
# ============================================================
# Description:
# This program demonstrates how multiple conditions can be
# evaluated using an if-elif-else statement. It compares
# three numbers and determines which one is the largest.
# ============================================================

# Prompt the user to enter three numbers
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# Determine the largest number
if first_number >= second_number and first_number >= third_number:
    print("The largest number is:", first_number)
elif second_number >= first_number and second_number >= third_number:
    print("The largest number is:", second_number)
else:
    print("The largest number is:", third_number)

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================