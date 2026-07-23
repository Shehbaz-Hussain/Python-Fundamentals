"""
Module 13 - Data Structures
Example 05: List Indexing

Purpose:
Demonstrate how to access list elements using
positive and negative indexing.
"""

# Create a list of AI subjects
ai_subjects = [
    "Python",
    "Mathematics",
    "Statistics",
    "Machine Learning",
    "Deep Learning"
]

# Display the complete list
print("AI Subjects:")
print(ai_subjects)

# Access elements using positive indexing
print("\nFirst subject:", ai_subjects[0])
print("Third subject:", ai_subjects[2])

# Access elements using negative indexing
print("Last subject:", ai_subjects[-1])
print("Second last subject:", ai_subjects[-2])

# Expected Output:
# AI Subjects:
# ['Python', 'Mathematics', 'Statistics', 'Machine Learning', 'Deep Learning']
#
# First subject: Python
# Third subject: Statistics
# Last subject: Deep Learning
# Second last subject: Machine Learning