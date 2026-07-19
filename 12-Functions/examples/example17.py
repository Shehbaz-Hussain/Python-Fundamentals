"""
File: 12-Functions/examples/example17.py
Topic: Marks Calculation Using Functions

Description:
This example demonstrates how functions can be used to calculate
the total marks, percentage, and pass/fail result of a student.
Each function performs one specific task, making the program
modular and easy to understand.
"""


def calculate_total(english, mathematics, science):
    """Return the total marks."""
    return english + mathematics + science


def calculate_percentage(total_marks, maximum_marks):
    """Return the percentage."""
    return (total_marks / maximum_marks) * 100


def get_result(percentage):
    """Return the student's result."""
    if percentage >= 40:
        return "Pass"
    return "Fail"


# Student marks
english_marks = 78
mathematics_marks = 85
science_marks = 69

maximum_marks = 300

# Perform calculations
total_marks = calculate_total(
    english_marks,
    mathematics_marks,
    science_marks
)

percentage = calculate_percentage(total_marks, maximum_marks)
result = get_result(percentage)

# Display the report
print("Student Marks Report")
print("--------------------")
print("English     :", english_marks)
print("Mathematics :", mathematics_marks)
print("Science     :", science_marks)
print()
print("Total Marks :", total_marks)
print(f"Percentage  : {percentage:.2f}%")
print("Result      :", result)