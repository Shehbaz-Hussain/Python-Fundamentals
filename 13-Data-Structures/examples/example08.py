"""
Module 13 - Data Structures
Example 08: Iterating Over a List

Purpose:
Demonstrate how to iterate over the elements of a list
using a for loop.
"""

# Create a list of programming languages
programming_languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "Go"
]

# Display the complete list
print("Programming Languages:")
print(programming_languages)

# Iterate over each element in the list
print("\nIterating over the list:")

for language in programming_languages:
    print(language)

# Display the total number of languages
print("\nTotal languages:", len(programming_languages))

# Expected Output:
# Programming Languages:
# ['Python', 'Java', 'C++', 'JavaScript', 'Go']
#
# Iterating over the list:
# Python
# Java
# C++
# JavaScript
# Go
#
# Total languages: 5