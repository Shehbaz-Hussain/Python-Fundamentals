"""
Module 13 - Data Structures
Example 19: Nested Data Structures

Purpose:
Demonstrate how to access data stored in nested data structures
using a dictionary that contains lists.
"""

# Create a dictionary where each key maps to a list of values.
student = {
    "name": "Alice",
    "subjects": ["Mathematics", "Physics", "Computer Science"],
    "marks": [88, 91, 95]
}

print("Student information:")
print(student)

# Access individual elements from the nested lists.
print("\nStudent name:", student["name"])
print("First subject:", student["subjects"][0])
print("Second subject:", student["subjects"][1])
print("Computer Science marks:", student["marks"][2])

# Expected Output:
# Student information:
# {'name': 'Alice', 'subjects': ['Mathematics', 'Physics', 'Computer Science'], 'marks': [88, 91, 95]}
#
# Student name: Alice
# First subject: Mathematics
# Second subject: Physics
# Computer Science marks: 95