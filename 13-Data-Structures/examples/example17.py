"""
Module 13 - Data Structures
Example 17: Using Built-in Functions with a List

Purpose:
Demonstrate how to use common built-in functions such as
len(), min(), max(), and sum() with a list of numbers.
"""

# Create a list of numbers.
numbers = [12, 8, 25, 17, 30]

print("List of numbers:")
print(numbers)

# Calculate the number of elements.
print("\nNumber of elements:", len(numbers))

# Find the smallest value.
print("Smallest value:", min(numbers))

# Find the largest value.
print("Largest value:", max(numbers))

# Calculate the sum of all values.
print("Sum of all values:", sum(numbers))

# Expected Output:
# List of numbers:
# [12, 8, 25, 17, 30]
#
# Number of elements: 5
# Smallest value: 8
# Largest value: 30
# Sum of all values: 92