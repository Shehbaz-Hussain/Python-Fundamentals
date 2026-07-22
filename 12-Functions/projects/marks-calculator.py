"""
Project: Marks Calculator

Description:
This project demonstrates how functions can be used to calculate
the total marks, percentage, and grade of a student.
"""


def calculate_total(mark1, mark2, mark3):
    """Return the total marks."""
    return mark1 + mark2 + mark3


def calculate_percentage(total_marks):
    """Return the percentage."""
    return (total_marks / 300) * 100


def calculate_grade(percentage):
    """Return the grade based on the percentage."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    else:
        return "F"


def main():
    """Run the marks calculator."""
    print("Student Marks Calculator")
    print("------------------------")

    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    total = calculate_total(mark1, mark2, mark3)
    percentage = calculate_percentage(total)
    grade = calculate_grade(percentage)

    print("\nResult")
    print("------")
    print(f"Total Marks: {total}/300")
    print(f"Percentage: {percentage:.2f}%")
    print(f"Grade: {grade}")


main()