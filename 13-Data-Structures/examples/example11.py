"""
Module 13 - Data Structures
Example 11: Updating Dictionary Values

Purpose:
Demonstrate how to update the value of an existing key in a dictionary.
"""

# Create a dictionary containing student information.
student = {
    "name": "Alice",
    "age": 20,
    "grade": "B"
}

print("Original dictionary:")
print(student)

# Update the value associated with an existing key.
student["grade"] = "A"

print("\nDictionary after updating the grade:")
print(student)

# Expected Output:
# Original dictionary:
# {'name': 'Alice', 'age': 20, 'grade': 'B'}
#
# Dictionary after updating the grade:
# {'name': 'Alice', 'age': 20, 'grade': 'A'}