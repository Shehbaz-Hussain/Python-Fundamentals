"""
Module 13 - Data Structures
Example 04: Creating and Accessing Dictionaries

Purpose:
Demonstrate how to create a dictionary, access values
using keys, and display information stored as key-value pairs.
"""

# Create a dictionary containing student information
student = {
    "name": "Ali",
    "age": 20,
    "program": "BSAI",
    "semester": 4
}

# Display the complete dictionary
print("Student Information:")
print(student)

# Access dictionary values using keys
print("\nName:", student["name"])
print("Age:", student["age"])
print("Program:", student["program"])
print("Semester:", student["semester"])

# Display the total number of key-value pairs
print("\nTotal fields:", len(student))

# Expected Output:
# Student Information:
# {'name': 'Ali', 'age': 20, 'program': 'BSAI', 'semester': 4}
#
# Name: Ali
# Age: 20
# Program: BSAI
# Semester: 4
#
# Total fields: 4