"""
Module 13 - Data Structures
Example 06: List Slicing

Purpose:
Demonstrate how to extract portions of a list
using different slicing techniques.
"""

# Create a list of numbers
numbers = [10, 20, 30, 40, 50, 60, 70]

# Display the original list
print("Original List:")
print(numbers)

# Slice the first three elements
print("\nFirst three elements:")
print(numbers[:3])

# Slice the middle elements
print("\nMiddle elements:")
print(numbers[2:5])

# Slice from the fourth element to the end
print("\nFrom the fourth element to the end:")
print(numbers[3:])

# Slice every second element
print("\nEvery second element:")
print(numbers[::2])

# Reverse the list using slicing
print("\nReversed list:")
print(numbers[::-1])

# Expected Output:
# Original List:
# [10, 20, 30, 40, 50, 60, 70]
#
# First three elements:
# [10, 20, 30]
#
# Middle elements:
# [30, 40, 50]
#
# From the fourth element to the end:
# [40, 50, 60, 70]
#
# Every second element:
# [10, 30, 50, 70]
#
# Reversed list:
# [70, 60, 50, 40, 30, 20, 10]