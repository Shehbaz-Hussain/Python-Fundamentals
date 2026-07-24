"""
Module 13 - Data Structures
Example 15: Iterating Over a Dictionary

Purpose:
Demonstrate how to iterate over the keys and values of a dictionary
using a for loop.
"""

# Create a dictionary containing student marks.
student_marks = {
    "Alice": 85,
    "Bob": 91,
    "Charlie": 78,
    "Diana": 88
}

print("Student Marks:")

# Iterate through the dictionary.
for student_name, marks in student_marks.items():
    print(f"{student_name}: {marks}")

# Expected Output:
# Student Marks:
# Alice: 85
# Bob: 91
# Charlie: 78
# Diana: 88