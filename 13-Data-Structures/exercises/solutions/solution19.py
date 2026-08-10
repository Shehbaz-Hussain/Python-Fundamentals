"""
Module 13 - Data Structures
Solution 19: Working with Nested Data Structures

Solution:
"""

# Create the classroom dictionary.
classroom = {
    "teacher": "Mr. Khan",
    "students": ["Ali", "Sara", "Ahmed", "Fatima"]
}

# Print the complete dictionary.
print(classroom)

# Print the teacher's name.
print(classroom["teacher"])

# Print the first student's name.
print(classroom["students"][0])

# Print the last student's name.
print(classroom["students"][-1])

# Print the total number of students.
print(len(classroom["students"]))