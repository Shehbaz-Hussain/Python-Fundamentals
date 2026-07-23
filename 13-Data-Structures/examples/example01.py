"""
Module 13 - Data Structures
Example 01: Creating and Displaying Lists

Purpose:
Demonstrate how to create a list, access its elements,
and display information about the list.
"""

# Create a list of programming languages
programming_languages = [
    "Python",
    "Java",
    "C++",
    "JavaScript"
]

# Display the complete list
print("Programming Languages:")
print(programming_languages)

# Display individual elements using indexing
print("\nFirst language:", programming_languages[0])
print("Second language:", programming_languages[1])
print("Third language:", programming_languages[2])
print("Fourth language:", programming_languages[3])

# Display the number of elements in the list
print("\nTotal languages:", len(programming_languages))

# Expected Output:
# Programming Languages:
# ['Python', 'Java', 'C++', 'JavaScript']
#
# First language: Python
# Second language: Java
# Third language: C++
# Fourth language: JavaScript
#
# Total languages: 4