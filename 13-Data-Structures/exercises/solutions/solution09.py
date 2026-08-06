"""
Module 13 - Data Structures
Solution 09: Updating Dictionary Values

Purpose:
Demonstrate how to update the value associated with an existing key
in a dictionary. This example shows that dictionaries are mutable,
meaning their contents can be modified after creation.
"""

# Create a dictionary representing a student's information.
student = {
    "name": "Ayesha",
    "age": 20,
    "course": "Artificial Intelligence"
}

print("Before Update:")
print(student)

# Update the value of an existing key.
student["age"] = 21

print("\nAfter Updating Age:")
print(student)

# Update another existing key.
student["course"] = "Machine Learning"

print("\nAfter Updating Course:")
print(student)

# Expected Output:
# Before Update:
# {'name': 'Ayesha', 'age': 20, 'course': 'Artificial Intelligence'}
#
# After Updating Age:
# {'name': 'Ayesha', 'age': 21, 'course': 'Artificial Intelligence'}
#
# After Updating Course:
# {'name': 'Ayesha', 'age': 21, 'course': 'Machine Learning'}