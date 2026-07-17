"""
Exercise 20: Student Scholarship Eligibility Checker

Problem Statement:
Write a Python program that asks the user to enter a student's percentage
and attendance percentage. Determine whether the student is eligible for
a scholarship.

Scholarship Eligibility Rules:
- The student must have a percentage of 85 or above.
- The student must have an attendance percentage of 90 or above.

Conditions:
- If both conditions are satisfied, the student is eligible for a scholarship.
- Otherwise, the student is not eligible.

Expected Output Examples:

Example 1:
Enter student's percentage: 91
Enter attendance percentage: 94
Scholarship Status: Eligible

Example 2:
Enter student's percentage: 82
Enter attendance percentage: 95
Scholarship Status: Not Eligible

Example 3:
Enter student's percentage: 90
Enter attendance percentage: 85
Scholarship Status: Not Eligible
"""

# Ask the user to enter the student's academic percentage
percentage = float(input("Enter student's percentage: "))

# Ask the user to enter the student's attendance percentage
attendance = float(input("Enter attendance percentage: "))

# Check scholarship eligibility
if percentage >= 85 and attendance >= 90:
    print("Scholarship Status: Eligible")
else:
    print("Scholarship Status: Not Eligible")