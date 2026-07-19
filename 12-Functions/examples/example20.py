"""
File: 12-Functions/examples/example20.py
Topic: Mini Real-World Example - Student Report Generator

Description:
This example demonstrates how multiple functions can work together
to solve a small real-world problem. The program calculates a
student's total marks, percentage, grade, and final result by
dividing the work into separate reusable functions.
"""


def calculate_total(english, mathematics, science):
    """Return the total marks obtained."""
    return english + mathematics + science


def calculate_percentage(total_marks, maximum_marks):
    """Return the percentage."""
    return (total_marks / maximum_marks) * 100


def calculate_grade(percentage):
    """Return the student's grade."""
    if percentage >= 90:
        return "A+"
    if percentage >= 80:
        return "A"
    if percentage >= 70:
        return "B"
    if percentage >= 60:
        return "C"
    if percentage >= 40:
        return "D"
    return "F"


def calculate_result(percentage):
    """Return the student's final result."""
    if percentage >= 40:
        return "Pass"
    return "Fail"


# Student data
student_name = "Ali"

english_marks = 85
mathematics_marks = 78
science_marks = 91

maximum_marks = 300

# Perform calculations
total_marks = calculate_total(
    english_marks,
    mathematics_marks,
    science_marks
)

percentage = calculate_percentage(total_marks, maximum_marks)
grade = calculate_grade(percentage)
result = calculate_result(percentage)

# Display the report
print("Student Report")
print("--------------")
print("Name        :", student_name)
print("English     :", english_marks)
print("Mathematics :", mathematics_marks)
print("Science     :", science_marks)
print()
print("Total Marks :", total_marks)
print(f"Percentage  : {percentage:.2f}%")
print("Grade       :", grade)
print("Result      :", result)