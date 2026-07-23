"""
Module 13 - Data Structures
Example 03: Creating and Using Sets

Purpose:
Demonstrate how to create a set, show that duplicate
elements are removed automatically, and check membership.
"""

# Create a set containing duplicate values
programming_languages = {
    "Python",
    "Java",
    "Python",
    "C++",
    "Java"
}

# Display the set
print("Programming Languages:")
print(programming_languages)

# Display the number of unique elements
print("\nTotal unique languages:", len(programming_languages))

# Check membership
print("\nIs 'Python' available?", "Python" in programming_languages)
print("Is 'JavaScript' available?", "JavaScript" in programming_languages)

# Expected Output:
# Programming Languages:
# {'Python', 'Java', 'C++'}
#
# Note:
# The order of elements in a set is not guaranteed.
# Your output may display the elements in a different order.
#
# Total unique languages: 3
#
# Is 'Python' available? True
# Is 'JavaScript' available? False