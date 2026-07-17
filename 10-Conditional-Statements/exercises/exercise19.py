"""
Exercise 19: Employee Bonus Eligibility Checker

Problem Statement:
Write a Python program that asks the user to enter an employee's years of
service and annual performance rating. Based on the entered information,
determine whether the employee is eligible for a bonus.

Bonus Eligibility Rules:
- The employee must have at least 5 years of service.
- The performance rating must be 4 or higher (out of 5).

Conditions:
- If both conditions are satisfied, the employee is eligible for a bonus.
- Otherwise, the employee is not eligible for a bonus.

Expected Output Examples:

Example 1:
Enter years of service: 8
Enter performance rating (1-5): 5
Bonus Status: Eligible

Example 2:
Enter years of service: 3
Enter performance rating (1-5): 5
Bonus Status: Not Eligible

Example 3:
Enter years of service: 7
Enter performance rating (1-5): 3
Bonus Status: Not Eligible
"""

# Ask the user to enter the years of service
years_of_service = int(input("Enter years of service: "))

# Ask the user to enter the performance rating
performance_rating = int(input("Enter performance rating (1-5): "))

# Check bonus eligibility
if years_of_service >= 5 and performance_rating >= 4:
    print("Bonus Status: Eligible")
else:
    print("Bonus Status: Not Eligible")