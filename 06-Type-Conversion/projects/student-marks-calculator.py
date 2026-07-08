"""
File: student-marks-calculator.py

Project: Student Marks Calculator

Difficulty:
Beginner

Description:
This project demonstrates how to use user input, type conversion,
variables, arithmetic operators, and the type() function.

The program asks the user to enter marks for three subjects,
converts the inputs into integers, calculates the total marks
and average marks, and displays the results.

Concepts Practiced:
- input()
- print()
- variables
- int()
- float()
- str()
- type()
- arithmetic operators (+, /)
"""

# =====================================
# Student Marks Calculator Project
# =====================================

print("=====================================")
print("    STUDENT MARKS CALCULATOR")
print("=====================================")

# Ask the user to enter marks for three subjects
subject1_text = input("Enter marks for Subject 1: ")
subject2_text = input("Enter marks for Subject 2: ")
subject3_text = input("Enter marks for Subject 3: ")

# Convert the inputs into integers
subject1 = int(subject1_text)
subject2 = int(subject2_text)
subject3 = int(subject3_text)

# Calculate the total marks
total_marks = subject1 + subject2 + subject3

# Calculate the average marks
average_marks = total_marks / 3

print()
print("========== RESULT ==========")

# Display the entered marks
print("Subject 1 Marks:", subject1)
print("Subject 2 Marks:", subject2)
print("Subject 3 Marks:", subject3)

print()

# Display the calculated values
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)

print()
print("========== DATA TYPES ==========")

# Display the data types
print("Subject 1 Type:", type(subject1))
print("Subject 2 Type:", type(subject2))
print("Subject 3 Type:", type(subject3))
print("Total Marks Type:", type(total_marks))
print("Average Marks Type:", type(average_marks))

print()
print("Thank you for using the Student Marks Calculator!")