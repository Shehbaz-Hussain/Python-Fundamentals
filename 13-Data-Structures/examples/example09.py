"""
Module 13 - Data Structures
Example 09: Iterating Over a Dictionary

Purpose:
Demonstrate how to iterate over the keys and values
of a dictionary using the items() method.
"""

# Create a dictionary containing student information
student = {
    "Name": "Ali",
    "Age": 20,
    "Program": "BSAI",
    "Semester": 4
}

# Display the complete dictionary
print("Student Information:")
print(student)

# Iterate over the dictionary
print("\nDictionary Contents:")

for key, value in student.items():
    print(f"{key}: {value}")

# Display the total number of key-value pairs
print("\nTotal fields:", len(student))

# Expected Output:
# Student Information:
# {'Name': 'Ali', 'Age': 20, 'Program': 'BSAI', 'Semester': 4}
#
# Dictionary Contents:
# Name: Ali
# Age: 20
# Program: BSAI
# Semester: 4
#
# Total fields: 4