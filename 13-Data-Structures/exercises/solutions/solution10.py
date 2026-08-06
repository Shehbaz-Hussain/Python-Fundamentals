"""
Module 13 - Data Structures
Solution 10: Iterating Over a Dictionary

Solution:
"""

# Create a dictionary named subjects.
subjects = {
    "Mathematics": 85,
    "Physics": 90,
    "Computer Science": 95
}

# Print the complete dictionary.
print(subjects)

# Iterate through the dictionary and print each
# subject with its corresponding marks.
for subject, marks in subjects.items():
    print(f"{subject}: {marks}")