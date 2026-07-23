"""
Module 13 - Data Structures
Example 02: Creating and Accessing Tuples

Purpose:
Demonstrate how to create a tuple, access its elements,
and show that tuples preserve the order of their values.
"""

# Create a tuple of weekdays
weekdays = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday"
)

# Display the complete tuple
print("Weekdays:")
print(weekdays)

# Access tuple elements using indexing
print("\nFirst day:", weekdays[0])
print("Third day:", weekdays[2])
print("Last day:", weekdays[-1])

# Display the total number of elements
print("\nTotal weekdays:", len(weekdays))

# Expected Output:
# Weekdays:
# ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
#
# First day: Monday
# Third day: Wednesday
# Last day: Friday
#
# Total weekdays: 5