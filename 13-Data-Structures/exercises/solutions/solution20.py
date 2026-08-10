"""
Module 13 - Data Structures
Solution 20: Combining Multiple Data Structures

Solution:
"""

# Create the subjects list.
subjects = ["Mathematics", "Physics", "Computer Science"]

# Create the semester_info tuple.
semester_info = (4, "Spring 2026")

# Create the clubs set.
clubs = {"Robotics", "AI", "Programming"}

# Create the student dictionary.
student = {
    "name": "Ayesha",
    "roll_number": 101,
    "cgpa": 3.75
}

# Print each data structure.
print(subjects)
print(semester_info)
print(clubs)
print(student)

# Print the first subject.
print(subjects[0])

# Print the semester number.
print(semester_info[0])

# Check whether "AI" is in the clubs set.
print("AI" in clubs)

# Print the student's name.
print(student["name"])