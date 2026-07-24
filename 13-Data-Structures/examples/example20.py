"""
Module 13 - Data Structures
Example 20: Choosing the Appropriate Data Structure

Purpose:
Demonstrate how different data structures (list, tuple, set,
and dictionary) are used to solve different types of problems.
"""

# A list stores an ordered collection of items.
courses = ["Python", "Data Structures", "Machine Learning"]

# A tuple stores fixed, immutable data.
software_version = (3, 13, 0)

# A set stores unique values.
skills = {"Python", "Git", "SQL", "Python"}

# A dictionary stores key-value pairs.
student = {
    "name": "Alice",
    "semester": 2,
    "cgpa": 3.82
}

print("List:")
print(courses)

print("\nTuple:")
print(software_version)

print("\nSet:")
print(skills)

print("\nDictionary:")
print(student)

# Expected Output:
# List:
# ['Python', 'Data Structures', 'Machine Learning']
#
# Tuple:
# (3, 13, 0)
#
# Set:
# {'Python', 'Git', 'SQL'}
# Note: The order of elements in a set is not guaranteed.
#
# Dictionary:
# {'name': 'Alice', 'semester': 2, 'cgpa': 3.82}