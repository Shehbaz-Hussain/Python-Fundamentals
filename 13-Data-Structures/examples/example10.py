"""
Module 13 - Data Structures
Example 10: Membership Operators with Data Structures

Purpose:
Demonstrate how to use the 'in' and 'not in'
membership operators with lists, tuples, sets,
dictionaries, and strings.
"""

# Create different data structures
programming_languages = [
    "Python",
    "Java",
    "C++"
]

weekdays = (
    "Monday",
    "Tuesday",
    "Wednesday"
)

ai_tools = {
    "TensorFlow",
    "PyTorch",
    "Scikit-learn"
}

student = {
    "name": "Ali",
    "semester": 4,
    "program": "BSAI"
}

text = "Artificial Intelligence"

# Membership test with a list
print("Python in programming_languages:")
print("Python" in programming_languages)

# Membership test with a tuple
print("\nFriday in weekdays:")
print("Friday" in weekdays)

# Membership test with a set
print("\nPyTorch in ai_tools:")
print("PyTorch" in ai_tools)

# Membership test with a dictionary
print("\n'name' in student:")
print("name" in student)

# Membership test with a string
print("\n'Intelligence' in text:")
print("Intelligence" in text)

# Using 'not in'
print("\nRust not in programming_languages:")
print("Rust" not in programming_languages)

# Expected Output:
# Python in programming_languages:
# True
#
# Friday in weekdays:
# False
#
# PyTorch in ai_tools:
# True
#
# 'name' in student:
# True
#
# 'Intelligence' in text:
# True
#
# Rust not in programming_languages:
# True
#
# Note:
# Dictionary membership checks keys by default.
# Set element order is not guaranteed, but membership results
# are always either True or False.