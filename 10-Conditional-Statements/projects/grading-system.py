"""
Project: Grading System

Description:
This program accepts a student's marks and determines
the corresponding grade using conditional statements.

Concepts Used:
- input()
- int()
- if
- elif
- else
- Comparison operators

Grading Criteria:
90–100 : A
80–89  : B
70–79  : C
60–69  : D
0–59   : F

Marks outside the range 0–100 are considered invalid.
"""

print("===== Grading System =====")

marks = int(input("Enter your marks (0-100): "))

if marks < 0 or marks > 100:
    print("Invalid marks. Please enter a value between 0 and 100.")

elif marks >= 90:
    print("Grade: A")

elif marks >= 80:
    print("Grade: B")

elif marks >= 70:
    print("Grade: C")

elif marks >= 60:
    print("Grade: D")

else:
    print("Grade: F")