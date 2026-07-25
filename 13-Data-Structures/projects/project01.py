"""
Module 13 - Data Structures
Project 01: Student Record Manager

Objective:
Build a simple student record manager that demonstrates the practical
use of Python data structures, including lists, tuples, sets, and
dictionaries.

Problem Statement:
A teacher wants to maintain basic information about students enrolled
in a class. The program should display student records, unique courses,
and basic statistics using appropriate data structures.

Requirements:
- Use a list to store student records.
- Use a dictionary for each student's information.
- Use a tuple to store marks.
- Use a set to store unique course names.
- Display all records in a readable format.
- Calculate and display the average marks for each student.
- Display the total number of students and unique courses.
"""

# List of student records
students = [
    {
        "name": "Ali",
        "age": 20,
        "course": "Python",
        "marks": (85, 90, 88),
    },
    {
        "name": "Sara",
        "age": 21,
        "course": "Artificial Intelligence",
        "marks": (92, 95, 91),
    },
    {
        "name": "Ahmed",
        "age": 22,
        "course": "Python",
        "marks": (78, 82, 80),
    },
]

# Store unique course names
unique_courses = set()

print("=" * 40)
print("Student Record Manager")
print("=" * 40)

for student in students:
    unique_courses.add(student["course"])

    marks = student["marks"]
    average_marks = sum(marks) / len(marks)

    print(f"Name   : {student['name']}")
    print(f"Age    : {student['age']}")
    print(f"Course : {student['course']}")
    print(f"Marks  : {marks}")
    print(f"Average: {average_marks:.2f}")
    print("-" * 40)

print("Unique Courses:")
# The order of elements in a set is not guaranteed.
print(unique_courses)

print()
print("Total Students:", len(students))
print("Total Unique Courses:", len(unique_courses))

# Expected Output:
# ========================================
# Student Record Manager
# ========================================
# Name   : Ali
# Age    : 20
# Course : Python
# Marks  : (85, 90, 88)
# Average: 87.67
# ----------------------------------------
# Name   : Sara
# Age    : 21
# Course : Artificial Intelligence
# Marks  : (92, 95, 91)
# Average: 92.67
# ----------------------------------------
# Name   : Ahmed
# Age    : 22
# Course : Python
# Marks  : (78, 82, 80)
# Average: 80.00
# ----------------------------------------
# Unique Courses:
# {'Python', 'Artificial Intelligence'}
# The order of elements in a set is not guaranteed.
#
# Total Students: 3
# Total Unique Courses: 2

# Possible Improvements:
# - Allow the user to enter student information.
# - Store additional fields such as student ID and email.
# - Search for a student by name.
# - Sort students by name or average marks.
# - Save and load records using file handling in a later module.