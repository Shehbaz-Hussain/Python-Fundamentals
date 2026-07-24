"""
Module 13 - Data Structures
Example 12: Adding New Key-Value Pairs to a Dictionary

Purpose:
Demonstrate how to add new key-value pairs to an existing dictionary
using assignment.
"""

# Create a dictionary with basic information.
employee = {
    "id": 101,
    "name": "John"
}

print("Original dictionary:")
print(employee)

# Add a new key-value pair.
employee["department"] = "Engineering"

# Add another new key-value pair.
employee["salary"] = 75000

print("\nDictionary after adding new key-value pairs:")
print(employee)

# Expected Output:
# Original dictionary:
# {'id': 101, 'name': 'John'}
#
# Dictionary after adding new key-value pairs:
# {'id': 101, 'name': 'John', 'department': 'Engineering', 'salary': 75000}kkkkkkkkkk