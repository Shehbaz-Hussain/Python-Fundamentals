"""
Project: Student Marks Calculator

This program calculates total marks and average marks.
"""

math_marks = float(input("Enter Math marks: "))
python_marks = float(input("Enter Python marks: "))
ai_marks = float(input("Enter AI marks: "))

total_marks = math_marks + python_marks + ai_marks
average_marks = total_marks / 3

print("Total Marks:", total_marks)
print("Average Marks:", average_marks)