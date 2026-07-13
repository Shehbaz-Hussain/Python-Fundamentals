# ============================================================
# Example 09: Determining the Day Category
# ============================================================
# Description:
# This program demonstrates how an if-elif-else statement can
# evaluate multiple conditions. Based on the entered day
# number, the program identifies whether it is the beginning,
# middle, or end of the week.
# ============================================================

# Prompt the user to enter a day number
day = int(input("Enter a day number (1-7): "))

# Determine the day category
if day == 1:
    print("It is the beginning of the week.")
elif day >= 2 and day <= 5:
    print("It is a weekday.")
elif day == 6 or day == 7:
    print("It is the weekend.")
else:
    print("Invalid day number.")

# This statement always executes
print("Program execution completed.")

# ============================================================
# End of Example
# ============================================================